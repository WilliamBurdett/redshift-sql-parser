from .reponse import Response
from .component import Component


class ValueList(Component):
    def __init__(self, component_string):
        super().__init__(component_string)

    def generate_response(self):
        values = self.sql.split(',')
        for value in values:
            value = value.strip()
            if not value.isdigit():  # It's a string!
                if not value[0] == '\'' and value[-1:] == '\'':
                    self.response = Response(
                        'Value List contains string with no quotes', 1)
                    return
        self.response = Response.okay()
