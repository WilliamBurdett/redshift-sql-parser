from .component import Component
from .reponse import Response
from .utility import spaces_encased_by_quotes


class ColumnList(Component):
    def __init__(self, component_string, asterisk_allowed):
        super().__init__(component_string)
        self.asterisk_allowed = asterisk_allowed

    def generate_response(self):
        if self.asterisk_allowed and self.sql.strip() == '*':
            self.response = Response.okay()
            return
        values = self.sql.split(',')
        for value in values:
            value = value.strip()
            sides = value.split('.')
            for side in sides:
                if not spaces_encased_by_quotes(side):
                    self.response = Response('ColumnList not properly made', 1)
                    return

        self.response = Response.okay()
