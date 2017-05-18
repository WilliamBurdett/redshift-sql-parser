import query
import unittest


class TestQuery(unittest.TestCase):

    def test_check_sql_list_happy_path(self):
        actual_input = 'hello, world'
        self.assertEqual(query.Query.check_sql_list(actual_input), 0)

    def test_check_sql_list_with_quotes_allowed(self):
        actual_input = 'hello, " world", john'
        self.assertEqual(query.Query.check_sql_list(actual_input, True), 0)

    def test_check_sql_list_with_quotes_not_allowed(self):
        actual_input = 'hello, " world", john'
        self.assertEqual(query.Query.check_sql_list(actual_input), 1)

    def test_is_reserved_returns_true(self):
        actual_input = 'SELECT'
        self.assertEqual(query.Query.is_reserved(actual_input), True)

    def test_is_reserved_returns_false(self):
        actual_input = 'woop'
        self.assertEqual(query.Query.is_reserved(actual_input), False)


class TestSelect(unittest.TestCase):

    def test_check_query_happy_path(self):
        actual_input = '''
        SELECT *
        FROM schema.table
        '''
        select = query.Select(actual_input)
        self.assertEqual(select.check_query(), 0)

if __name__ == '__main__':
    unittest.main()