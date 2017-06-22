from .component import Component


class ValueList(Component):
    def __init__(self, component_string):
        super().__init__(component_string)

    def check_validity(self):
        values = self.sql.split(',')
        for value in values:
            value = value.strip()
            if not value.isdigit():  # It's a string!
                if not value[0] == '\'' and value[-1:] == '\'':
                    return 1
        return 0
