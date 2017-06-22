from sql_parser.conditional import Conditional
from unittest import TestCase, main

from sql_parser.reponse import Response


class TestConditional(TestCase):

    def test_check_conditional_happy_path(self):
        actual_input = ''' greater > lesser '''
        actual_conditional = Conditional(actual_input)
        self.assertEqual(actual_conditional.check_validity(), Response.okay())

    def test_check_conditional_no_spaces(self):
        """No spaces implies that the columns are adjacent to the AND/OR"""
        actual_input = '''greater > lesser'''
        actual_conditional = Conditional(actual_input)
        self.assertEqual(actual_conditional.check_validity(),
                         Response('No space between operator and field', 1))

if __name__ == '__main__':
    main()
