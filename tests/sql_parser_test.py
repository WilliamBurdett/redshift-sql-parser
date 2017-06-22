from sql_parser import sql_parser
from unittest import TestCase, main


class TestSqlParser(TestCase):

    def test_happy_path(self):
        actual_input = '''
        SELECT *
        FROM schema.table
        '''
        self.assertEqual(sql_parser.run_parser(actual_input), 0)

if __name__ == '__main__':
    main()
