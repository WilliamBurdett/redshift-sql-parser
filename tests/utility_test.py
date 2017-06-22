from unittest import TestCase, main

from sql_parser import utility


class TestCheckSpacesEncasedByQuotes(TestCase):
    def test_no_space_no_quote_return_true(self):
        actual_input = 'asdf'
        self.assertTrue(utility.spaces_encased_by_quotes(actual_input))

    def test_yes_space_no_quote_return_false(self):
        actual_input = 'as df'
        self.assertFalse(utility.spaces_encased_by_quotes(actual_input))

    def test_no_space_yes_quote_return_true(self):
        actual_input = '"asdf"'
        self.assertTrue(utility.spaces_encased_by_quotes(actual_input))

    def test_yes_space_yes_quote_return_true(self):
        actual_input = '"as df"'
        self.assertTrue(utility.spaces_encased_by_quotes(actual_input))

    def test_the_word_schema(self):
        actual_input = 'schema'
        self.assertTrue(utility.spaces_encased_by_quotes(actual_input))


class TestGetStringBetweenSubstrings(TestCase):
    def test_happy_path(self):
        actual_input = 'lalawootbobo'
        expected_output = 'woot'
        self.assertEquals(utility.get_string_between_substrings(actual_input, 'lala', 'bobo'),
                          expected_output)

    def test_keeps_whitespace_characters(self):
        actual_input = 'lala\nwoot\tbobo'
        expected_output = '\nwoot\t'
        self.assertEquals(utility.get_string_between_substrings(actual_input, 'lala', 'bobo'),
                          expected_output)


class TestRemoveAllWhitespaceCharacters(TestCase):
    def test_happy_path(self):
        actual_input = ' f d s  dsdfds\n\td'
        expected_output = 'fdsdsdfdsd'
        self.assertEquals(
            utility.remove_all_whitespace_characters(actual_input),
            expected_output)


class TestGetStringAfterSubstring(TestCase):
    def test_happy_path(self):
        actual_input_string = 'hello world my name is John'
        actual_input_substring = 'world'
        expected_output = ' my name is John'
        self.assertEquals(
            utility.get_string_after_substring(actual_input_string,
                                               actual_input_substring),
            expected_output)

    def test_empty_substring(self):
        actual_input_string = 'hello world my name is John'
        actual_input_substring = ''
        expected_output = 'hello world my name is John'
        self.assertEquals(
            utility.get_string_after_substring(actual_input_string,
                                               actual_input_substring),
            expected_output)


class GetNextSection(TestCase):
    def test_returns_brackets(self):
        actual_input = 'FROM (hello world) WHERE test'
        current_keyword = 'FROM'
        optional_keywords = []
        expected_output = '(hello world)'
        self.assertEquals(
            utility.get_next_section(actual_input, current_keyword,
                                     optional_keywords), expected_output)

    def test_returns_value(self):
        actual_input = 'FROM hello.world WHERE test'
        current_keyword = 'FROM'
        optional_keywords = ['WHERE']
        expected_output = ' hello.world '
        self.assertEquals(
            utility.get_next_section(actual_input, current_keyword,
                                     optional_keywords), expected_output)

    def test_returns_value_soonest(self):
        actual_input = 'FROM hello.world JOIN tree WHERE hug'
        current_keyword = 'FROM'
        optional_keywords = ['WHERE', 'JOIN']
        expected_output = ' hello.world '
        self.assertEquals(
            utility.get_next_section(actual_input, current_keyword,
                                     optional_keywords), expected_output)


if __name__ == '__main__':
    main()
