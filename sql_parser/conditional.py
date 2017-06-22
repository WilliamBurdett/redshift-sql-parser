from .utility import check_bracket_order
from .component import Component
from .reponse import Response


class Conditional(Component):
    operators = ['>=', '<=', '!=', '=', '>', '<']

    def generate_response(self):
        if not self.sql[0].isspace():
            self.response = Response('No space between operator and field', 1)
        elif not self.sql[-1:].isspace():
            self.response = Response('No space between operator and field', 1)
        fields = []
        for operator in self.operators:
            if operator in self.sql:
                fields = self.sql.split(operator)
                break
        if len(fields) != 2:
            self.response = Response('Too many fields', 1)
        if self.response is None:
            self.response = Response.okay()


class ConditionalSection(Component):
    def generate_response(self):
        response = check_bracket_order(self.sql)
        if response != Response.okay():
            self.response = response
            return

        # Once we check the bracket format, they are unimportant on
        # if the query will compile
        bracket_replaced = self.sql.replace('(', ' ') \
            .replace(')', ' ')
        conditionals = []
        for and_split in bracket_replaced.split('AND'):
            for or_split in and_split.split('OR'):
                conditionals.append(Conditional(or_split))
        for conditional in conditionals:
            response = conditional.check_validity()
            if response != Response.okay():
                self.response = response
                return
        self.response = Response.okay()
