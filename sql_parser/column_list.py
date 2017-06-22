from .component import Component
from .utility import spaces_encased_by_quotes


class ColumnList(Component):
    def __init__(self, component_string, asterisk_allowed):
        super().__init__(component_string)
        self.asterisk_allowed = asterisk_allowed

    def check_validity(self):
        if self.asterisk_allowed and self.sql.strip() == '*':
            self.is_valid = True
            return 0
        values = self.sql.split(',')
        for value in values:
            value = value.strip()
            sides = value.split('.')
            for side in sides:
                if not spaces_encased_by_quotes(side):
                    self.is_valid = False
                    return 1

        self.is_valid = True
        return 0
