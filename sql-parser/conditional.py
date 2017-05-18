from utility import check_bracket_order


class Conditional:
    def __init__(self, conditional_string):
        self.conditional = conditional_string

    def check_conditional(self):
        
        return 2


class ConditionalSection:
    def __init__(self, conditional_section):
        self.conditional_section = conditional_section

    def check_conditionals(self):
        check_bracket_order(self.conditional_section)

        conditionals = []
        for and_split in self.conditional_section.split('AND'):
            for or_split in and_split.split('OR'):
                conditionals.append(Conditional(or_split))
        for conditional in conditionals:
            if conditional.check_conditional() == 1:
                return 1
        return 0
