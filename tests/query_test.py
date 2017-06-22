from sql_parser.query import Query, Select
from unittest import TestCase, main

from sql_parser.reponse import Response


class TestQuery(TestCase):

    def test_is_reserved_returns_true(self):
        actual_input = 'SELECT'
        self.assertEquals(Query.is_reserved(actual_input), True)

    def test_is_reserved_returns_false(self):
        actual_input = 'woop'
        self.assertEquals(Query.is_reserved(actual_input), False)


class TestSelect(TestCase):

    def test_check_query_happy_path(self):
        actual_input = '''
        SELECT *
        FROM schema.table
        '''
        select = Select(actual_input)
        select.check_validity()
        self.assertEquals(select.response, Response.okay())

    def test_check_query_unhappy_path(self):
        actual_input = '''
        SELECT lala,lalala  dfsdf
        FROM schema.table
        '''
        select = Select(actual_input)
        select.check_validity()
        self.assertEquals(select.response,
                          Response('ColumnList not properly made',1))

    def test_check_inner_query(self):
        actual_input = '''
        SELECT lala,lalala
        FROM (SELECT * FROM lalaland)
        '''
        select = Select(actual_input)
        select.check_validity()
        self.assertEquals(select.response, Response.okay())


if __name__ == '__main__':
    main()
