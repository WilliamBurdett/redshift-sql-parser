class Response:
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def print_error(self):
        print(self.message)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return (self.code == other.code and
                    self.message == other.message)
        return False

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

    def __str__(self):
        return 'Code: ' + str(self.code) + ' Message: ' + self.message

    @staticmethod
    def okay() -> object:
        return Response('Okay', 0)
