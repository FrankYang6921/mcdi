from abc import abstractmethod

from mid.core import InGameGenerator


class Middle(object):
    __dependencies__ = []
    __conflicts__ = []

    __author__ = "undefined"

    @abstractmethod
    def exec(self, generator: InGameGenerator) -> None:
        pass

    @abstractmethod
    def init(self, generator: InGameGenerator) -> None:
        pass

    @abstractmethod
    def dependency_connect(self, dependencies):
        pass
