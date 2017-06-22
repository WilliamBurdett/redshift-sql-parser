from conditional import Conditional
from unittest import TestCase, main


class TestConditional(TestCase):

    def test_check_conditional_happy_path(self):
        actual_input = ''' greater > lesser '''
        actual_conditional = Conditional(actual_input)
        self.assertEqual(actual_conditional.check_validity(), 0)

    def test_check_conditional_no_spaces(self):
        """No spaces implies that the columns are adjacent to the AND/OR"""
        actual_input = '''greater > lesser'''
        actual_conditional = Conditional(actual_input)
        self.assertEqual(actual_conditional.check_validity(), 1)

if __name__ == '__main__':
    main()
