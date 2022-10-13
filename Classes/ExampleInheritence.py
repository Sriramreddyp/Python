from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream id already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream id already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


# class MemoryStream(Stream):


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from Newtwork Stream")
