class ParseError:
    def __init__(self, message):
        self.message = message

    def print_error(self):
        print(self.message)