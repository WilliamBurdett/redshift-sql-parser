from abc import ABCMeta, abstractmethod


class Component:
    __metaclass__ = ABCMeta

    def __init__(self, component_string):
        self.sql = component_string
        self.is_valid = None

    @abstractmethod
    def check_validity(self):
        pass
