from abc import ABCMeta, abstractmethod


class Component:
    __metaclass__ = ABCMeta

    def __init__(self, component_string):
        self.sql = component_string
        self.response = None

    def check_validity(self):
        if self.response is not None:
            return self.response
        self.generate_response()
        return self.response

    @abstractmethod
    def generate_response(self):
        pass
