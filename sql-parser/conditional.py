from utility import check_bracket_order
from component import Component


class Conditional(Component):
    operators = ['>=', '<=', '!=', '=', '>', '<']

    def check_validity(self):
        if not self.sql[0].isspace():
            return 1
        elif not self.sql[-1:].isspace():
            return 1
        fields = []
        for operator in self.operators:
            if operator in self.sql:
                fields = self.sql.split(operator)

        return 2


class ConditionalSection(Component):
    def check_validity(self):
        if check_bracket_order(self.sql) == 1:
            return 1

        # Once we check the bracket format, they are unimportant on
        # if the query will compile
        bracket_replaced = self.sql.replace('(', ' ') \
            .replace(')', ' ')
        conditionals = []
        for and_split in bracket_replaced.split('AND'):
            for or_split in and_split.split('OR'):
                conditionals.append(Conditional(or_split))
        for conditional in conditionals:
            if conditional.check_conditional() == 1:
                return 1
        return 0
