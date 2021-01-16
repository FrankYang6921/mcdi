import sys
from base64 import b64encode
from operator import itemgetter

sys.path.append("..")
from mid.klass import *


class InGameGenerator(BaseCbGenerator):
    def __init__(self, frontend, middles=None, *args, **kwargs):
        if middles is None:
            self.middles = []
        else:
            self.middles = list(middles)
        self.frontend = frontend(self)

        # Load variables
        self.prog_enabled = True
        self.gvol_enabled = True
        self.phase_enabled = True
        self.pitch_enabled = False
        self.volume_factor = 1
        self.pitch_factor = 2
        self.pitch_base = 8192

        self.note_links = {}

        super(InGameGenerator, self).__init__(*args, **kwargs)

    def _init_middle_status(self):
        for middle in self.middles:
            for dependency in middle.__dependencies__:
                assert dependency in list(
                    map(type, self.middles)), f"Dependency {dependency} of {middle} is required, but not found."
            middle.dependency_connect(filter(lambda x: type(x) in middle.__dependencies__, self.middles))
            for conflict in middle.__conflicts__:
                assert conflict not in list(
                    map(type, self.middles)), f"Conflict {conflict} of {middle} is strictly forbidden, but found."
            middle.init(self)

    def make_note_links(self):
        logging.info("Making on-off note links.")

        self.note_links.clear()
        sustain_msgs, timestamp = [], 0

        program_mapping, volume_mapping, phase_mapping, pitch_mapping = {}, {}, {}, {}

        for index, message in enumerate(self):
            timestamp += message.time * self.tick_rate / self.tick_scale

            if message.type == "note_on":
                vars(message)["on_time"] = timestamp
                vars(message)["ch_note"] = (
                    message.channel, message.note
                )
                vars(message)["link_index"] = index
                vars(message)["context"] = program_mapping, volume_mapping, phase_mapping, pitch_mapping

                sustain_msgs.append(message)

            elif message.type == "note_off":
                try:
                    old_msg = next(filter(lambda p: p.ch_note == (message.channel, message.note), sustain_msgs))
                except StopIteration:
                    logging.warning(f"Bad MIDI file: off-note#{index} does not match on-note!")
                    continue

                old_index = _ = old_msg.link_index
                self.note_links[old_index] = (
                    timestamp, old_msg.on_time, message
                )
                self.note_links[index] = (
                    timestamp, old_msg.on_time, old_msg
                )

                sustain_msgs.remove(old_msg)

            elif "prog" in message.type:
                program_mapping[message.channel] = {"value": message.program, "time": timestamp}

            elif "control" in message.type:

                if message.control == 7:  # Volume change
                    volume_mapping[message.channel] = {"value": message.value, "time": timestamp}

                elif message.control == 121:  # No volume change
                    volume_mapping[message.channel] = {"value": 1.0, "time": timestamp}  # Recover

                elif message.control == 10:  # Phase change
                    phase_mapping[message.channel] = {"value": message.value, "time": timestamp}

            elif "pitch" in message.type:  # Pitch change
                pitch_mapping[message.channel] = {"value": message.pitch, "time": timestamp}

        logging.info(f"{len(self.note_links)} on-off note links made.")

    def load_messages(self):
        logging.info("Loading message(s) from the MIDI file.")

        # Clear loaded items
        self.loaded_messages.clear()
        self._init_middle_status()

        timestamp = message_count = 0

        program_mapping, volume_mapping, phase_mapping, pitch_mapping = {}, {}, {}, {}

        for index, message in enumerate(self):
            if message.is_meta:
                if message.type == "time_signature":
                    logging.info(f"MIDI file timing info: {message.numerator}/{message.denominator}.")
                elif message.type == "key_signature":
                    logging.info(f"MIDI file pitch info: {message.key}.")
                elif message.type in ("text", "copyright"):
                    logging.info(f"MIDI META message: {message.text}.")
                continue

            tick_time = round(
                (timestamp + message.time) * self.tick_rate / self.tick_scale
            )
            self.loaded_tick_count = max(self.loaded_tick_count, tick_time)

            if "note" in message.type:  # Note_on / note_off
                if message.channel in program_mapping.keys() and self.prog_enabled:  # Set program
                    program = program_mapping[message.channel]["value"] + 1
                else:
                    program = 1

                program = 0 if message.channel == 9 else program

                if message.channel in volume_mapping.keys() and self.gvol_enabled:  # Set volume
                    volume = volume_mapping[message.channel]["value"] / 127
                else:
                    volume = 1  # Max volume

                volume_value = volume * message.velocity * self.volume_factor

                if message.channel in pitch_mapping.keys() and self.pitch_enabled:  # Set pitch
                    pitch = pitch_mapping[message.channel]["value"]
                else:
                    pitch = self.pitch_base  # No pitch

                pitch_value = 2 ** ((pitch / self.pitch_base - 1) * self.pitch_factor / 12)

                if message.channel in phase_mapping.keys() and self.phase_enabled:  # Set phase
                    phase = phase_mapping[message.channel]["value"]
                else:
                    phase = 64  # Middle phase

                linked = self.note_links[index] if index in self.note_links.keys() else None

                self.loaded_messages.append({
                    "type": message.type,
                    "ch": message.channel,
                    "note": message.note,
                    "tick": tick_time,
                    "program": program,
                    "v": volume_value,
                    "pitch": pitch_value,
                    "phase": phase,
                    "linked": linked,
                })

                message_count += 1

            elif "prog" in message.type:
                program_mapping[message.channel] = {"value": message.program, "time": tick_time}

            elif "control" in message.type:

                if message.control == 7:  # Volume change
                    volume_mapping[message.channel] = {"value": message.value, "time": tick_time}

                elif message.control == 121:  # No volume change
                    volume_mapping[message.channel] = {"value": 1.0, "time": tick_time}  # Recover

                elif message.control == 10:  # Phase change
                    phase_mapping[message.channel] = {"value": message.value, "time": tick_time}

            elif "pitch" in message.type:  # Pitch change
                pitch_mapping[message.channel] = {"value": message.pitch, "time": tick_time}

            timestamp += message.time

            for middle in self.middles:  # Execute middleware
                middle.exec(self)

        self.loaded_messages = deque(sorted(self.loaded_messages, key=itemgetter("tick")))
        logging.info(f"Load procedure finished. {len(self.loaded_messages)} event(s) loaded.")

    def build_messages(self):
        logging.info(f'Building {len(self.loaded_messages)} event(s) loaded.')

        self._reset_build_status()
        self._init_plugin_status()

        for self.tick_index in range(-self.blank_ticks, self.loaded_tick_count + 1):
            self._update_build_status()

            while (messages := self.loaded_messages) and messages[0]["tick"] == self.tick_index:
                self.tick_cache.append(self.loaded_messages.popleft())  # Deque object is used to improve performance

            self._update_farray_status()

            for i, message in enumerate(self.tick_cache):
                if i > self.single_tick_limit and not (self.is_first_tick or self.is_last_tick):
                    break
                if message["type"] == "note_on":
                    self.add_tick_command(command=self.get_play_cmd(message))
                elif message["type"] == "note_off":
                    self.add_tick_command(command=self.get_stop_cmd(message))

            for plugin in self.plugins:  # Execute plugin
                plugin.exec(self)

            self._execute_schedules()
            self._reload_build_status()

            if self.tick_index % 100 == 0:  # Show progress
                logging.info(f"Built {self.tick_index} tick(s), {self.loaded_tick_count + 1} tick(s) in all.")

        logging.info(f"Build procedure finished. {len(self.built_function)} command(s) built.")

    def get_play_cmd(self, message):
        return self.frontend.get_play_cmd(**message)

    def get_stop_cmd(self, message):
        return self.frontend.get_stop_cmd(**message)

    # Plugin APIs

    def on_notes(self, ch=None):
        return list(filter(
            lambda message: message["type"] == "note_on" and (message["ch"] == ch if ch is not None else True),
            self.loaded_messages))  # Every tick

    def off_notes(self, ch=None):
        return list(filter(
            lambda message: message["type"] == "note_off" and (message["ch"] == ch if ch is not None else True),
            self.loaded_messages))  # Every tick

    def current_on_notes(self, ch=None):
        return list(filter(
            lambda message: message["type"] == "note_on" and (message["ch"] == ch if ch is not None else True),
            self.tick_cache))  # Only for this tick

    def current_off_notes(self, ch=None):
        return list(filter(
            lambda message: message["type"] == "note_off" and (message["ch"] == ch if ch is not None else True),
            self.tick_cache))  # Only for this tick

    def _future_notes(self, type_, tick, ch=None):
        for message in self.loaded_messages:
            if message["type"] != type_:
                continue
            if message["tick"] < tick:
                continue
            if message["tick"] == tick and (message["ch"] == ch if ch is not None else True):
                yield message
            if message["tick"] > tick:
                break

    def future_on_notes(self, tick, ch=None):
        return list(self._future_notes("note_on", ch))

    def future_off_notes(self, tick, ch=None):
        return list(self._future_notes("note_off", ch))


class RealTimeGenerator(BaseCbGenerator):
    IN_GAME_COMPATIBLE = {"program": 0, "v": 127, "pitch": 1, "phase": 64, "linked": None}

    def __init__(self, *args, **kwargs):
        super(RealTimeGenerator, self).__init__(*args, **kwargs)

    def load_messages(self):
        logging.info("Loading message(s) from the MIDI file.")

        # Clear loaded items
        self.loaded_messages.clear()
        timestamp = message_count = 0

        for index, message in enumerate(self):
            if message.is_meta:
                if message.type == "time_signature":
                    logging.info(f"MIDI file timing info: {message.numerator}/{message.denominator}.")
                elif message.type == "key_signature":
                    logging.info(f"MIDI file pitch info: {message.key}.")
                elif message.type in ("text", "copyright"):
                    logging.info(f"MIDI META message: {message.text}.")
                continue

            tick_time = (
                    (timestamp + message.time) * self.tick_rate / self.tick_scale
            )
            self.loaded_tick_count = max(self.loaded_tick_count, int(tick_time))

            delta_time = (tick_time - int(tick_time)) / self.tick_rate * self.tick_scale

            message_dict = {
                "msg": message.bin(),
                "tick": int(tick_time),
                "delta": delta_time,
                "type": message.type,
            }

            if "note" in message.type:
                message_dict["igc"] = {
                    "type": message.type, "ch": message.channel, "note": message.note, "tick": tick_time,
                }  # Compatibility for in-game plugins~
                message_dict["igc"].update(self.IN_GAME_COMPATIBLE)

            message_count += 1

            self.loaded_messages.append(message_dict)

            timestamp += message.time

        self.loaded_messages = deque(sorted(self.loaded_messages, key=itemgetter("tick")))
        logging.info(f"Load procedure finished. {len(self.loaded_messages)} event(s) loaded.")

    def build_messages(self):
        logging.info(f'Building {len(self.loaded_messages)} event(s).')

        self._reset_build_status()
        self._init_plugin_status()

        for self.tick_index in range(-self.blank_ticks, self.loaded_tick_count + 1):
            self._update_build_status()

            while (messages := self.loaded_messages) and messages[0]["tick"] == self.tick_index:
                self.tick_cache.append(self.loaded_messages.popleft())  # Deque object is used to improve performance

            self._update_farray_status()

            for i, message in enumerate(self.tick_cache):
                if i > self.single_tick_limit and not (self.is_first_tick or self.is_last_tick):
                    break
                self.add_tick_command(
                    command=f'mopp device send raw "{b64encode(message["msg"]).decode()}"'
                )

            for plugin in self.plugins:  # Execute plugin
                plugin.exec(self)

            self._execute_schedules()
            self._reload_build_status()

            if self.tick_index % 100 == 0:  # Show progress
                logging.info(f"Built {self.tick_index} tick(s), {self.loaded_tick_count + 1} tick(s) in all.")

        logging.info(f"Build procedure finished. {len(self.built_function)} command(s) built.")

    # Plugin APIs

    def on_notes(self, ch=None):
        return list(map(itemgetter("igc"),
                        filter(lambda message: message["type"] == "note_on" and (
                            (message["igc"]["ch"] == ch if ch is not None else True)), self.loaded_messages)
                        )
                    )  # Every tick

    def off_notes(self, ch=None):
        return list(map(itemgetter("igc"),
                        filter(lambda message: message["type"] == "note_off" and (
                            (message["igc"]["ch"] == ch if ch is not None else True)), self.loaded_messages)
                        )
                    )  # Every tick

    def current_on_notes(self, ch=None):
        return list(map(itemgetter("igc"),
                        filter(lambda message: message["type"] == "note_on" and (
                            (message["igc"]["ch"] == ch if ch is not None else True)), self.tick_cache)
                        )
                    )  # Only for this tick

    def current_off_notes(self, ch=None):
        return list(map(itemgetter("igc"),
                        filter(lambda message: message["type"] == "note_off" and (
                            (message["igc"]["ch"] == ch if ch is not None else True)), self.tick_cache)
                        )
                    )  # Only for this tick

    def _future_notes(self, type_, tick, ch=None):
        for message in self.loaded_messages:
            if message["type"] != type_:
                continue
            if message["tick"] < tick:
                continue
            if message["tick"] == tick and (message["igc"]["ch"] == ch if ch is not None else True):
                yield message["igc"]
            if message["tick"] > tick:
                break

    def future_on_notes(self, tick, ch=None):
        return list(self._future_notes("note_on", tick, ch))

    def future_off_notes(self, tick, ch=None):
        return list(self._future_notes("note_off", tick, ch))


__all__ = ["InGameGenerator", "RealTimeGenerator"]

if __name__ == '__main__':
    from mid.plugins import tweaks, piano, title

    logging.basicConfig(level=logging.INFO)

    generator = RealTimeGenerator(fp=r"D:\音乐\Midi Files\Without You（完美佳作）.mid", plugins=[
        tweaks.FixedTime(
            value=18000
        ),
        tweaks.FixedRain(
            value="clear"
        ),
        piano.PianoRoll(
            block_type="wool"
        ),
        piano.PianoRollFirework(),
        piano.PianoRollRenderer(
            [
                {
                    "funcs": [
                        {
                            "instance": piano.PowerFunctionPreset(),
                            "dot_dist": .1,
                        }
                    ],
                    "channels": [5],
                    "tracks": [],
                }
            ]
        ),
        tweaks.ProgressBar(
            text="进度条丨Progress Bar"
        ),
        title.MainTitle(
            [
                {
                    "text": "Without You",
                    "color": "blue"
                }
            ], {
                "text": "AVICII Forever"
            }
        ),
        tweaks.Viewport(
            *tweaks.Viewport.PRESET2
        ),
    ], single_tick_limit=2 ** 31 - 1)
    generator.auto_tick_rate(base=30)
    generator.load_messages()
    generator.build_messages()
    generator.write_datapack(r"D:\Minecraft\.minecraft\versions\fabric-loader-0.9.2+build.206-1.16.2\saves\MCDI")
