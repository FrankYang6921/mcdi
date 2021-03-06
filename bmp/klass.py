import logging
import sys
from abc import abstractmethod

from PIL import Image

sys.path.append("..")
from base.minecraft_types import *


class BaseGenerator(object):
    def __init__(self, fp, width=256, height=144, namespace="mcdi", func="bmp"):
        logging.info(f"Initializing. Loading bitmap: {fp}.")

        self.img = Image.open(fp=fp)
        self.x = width
        self.y = height
        self.built_function = Function(namespace, func)

    @abstractmethod
    def build_pixels(self, resample=Image.LANCZOS):
        pass

    def write_datapack(self, *args, **kwargs):
        logging.info(f"Writing {len(self.built_function)} command(s) built.")
        self.built_function.to_pack(*args, **kwargs)
        logging.info("Write procedure finished.")
