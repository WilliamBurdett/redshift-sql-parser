from query import Query, Select
import unittest


class TestQuery(unittest.TestCase):

    def test_check_sql_list_happy_path(self):
        actual_input = 'hello, world'
        self.assertEqual(Query.check_sql_list(actual_input), 0)

    def test_check_sql_list_with_quotes_allowed(self):
        actual_input = 'hello, " world", john'
        self.assertEqual(Query.check_sql_list(actual_input, True), 0)

    def test_check_sql_list_with_quotes_not_allowed(self):
        actual_input = 'hello, " world", john'
        self.assertEqual(Query.check_sql_list(actual_input), 1)

    def test_is_reserved_returns_true(self):
        actual_input = 'SELECT'
        self.assertEqual(Query.is_reserved(actual_input), True)

    def test_is_reserved_returns_false(self):
        actual_input = 'woop'
        self.assertEqual(Query.is_reserved(actual_input), False)

    def test_get_bracket_groupings_happy_path(self):
        actual_input = '((Z AND Z) AND Z) AND ((C AND D) AND (E AND F))'

        def hello(inside):
            print()
        
        self.assertEqual(Query.get_bracket_groupings(actual_input, hello), 0)


class TestSelect(unittest.TestCase):

    def test_check_query_happy_path(self):
        actual_input = '''
        SELECT *
        FROM schema.table
        '''
        select = Select(actual_input)
        self.assertEqual(select.check_query(), 0)

if __name__ == '__main__':
    unittest.main()
