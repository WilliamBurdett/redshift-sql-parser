import sql_parser
import unittest


class TestSqlParser(unittest.TestCase):

    def test_happy_path(self):
        actual_input = '''
        SELECT *
        FROM schema.table
        '''
        self.assertEqual(sql_parser.run_parser(actual_input), 0)

if __name__ == '__main__':
    unittest.main()