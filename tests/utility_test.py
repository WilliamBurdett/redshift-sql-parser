import utility
import unittest


class TestFindBetween(unittest.TestCase):

    def test_happy_path(self):
        actual_input = 'lalawootbobo'
        expected_output = 'woot'
        self.assertEquals(utility.find_between(actual_input, 'lala', 'bobo'), expected_output)

    def test_keeps_whitespace_characters(self):
        actual_input = 'lala\nwoot\tbobo'
        expected_output = '\nwoot\t'
        self.assertEquals(utility.find_between(actual_input, 'lala', 'bobo'), expected_output)
        

class TestRemoveAllWhitespaceCharacters(unittest.TestCase):
    
    def test_happy_path(self):
        actual_input = ' f d s  dsdfds\n\td'
        expected_output = 'fdsdsdfdsd'
        self.assertEqual(utility.remove_all_whitespace_characters(actual_input), expected_output)


class TestGetStringAfterSubstring(unittest.TestCase):

    def test_happy_path(self):
        actual_input_string = 'hello world my name is John'
        actual_input_substring = 'world'
        expected_output = ' my name is John'
        self.assertEqual(utility.get_string_after_substring(actual_input_string, actual_input_substring), expected_output)

if __name__ == '__main__':
    unittest.main()
