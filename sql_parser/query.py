from .component import Component
from .table_name import TableName
from .utility import get_string_between_substrings, \
    get_string_after_substring, \
    get_next_section
from .column_list import ColumnList
from .reponse import Response
from abc import ABCMeta, abstractmethod
from .reserved_keywords import reserved_keywords


def query_factory(sql):
    trimmed = sql.strip()
    if trimmed.index('SELECT') == 0:
        return Select(sql)
    elif trimmed.index('WITH') == 0:
        return With(sql)
    elif trimmed.index('INSERT') == 0:
        return Insert(sql)
    else:
        return Response('Failure to read query', 1)


class Query:
    __metaclass__ = ABCMeta

    def __init__(self, sql):
        self.sql = sql

    @abstractmethod
    def check_query(self):
        pass

    @staticmethod
    def is_reserved(string):
        if string in reserved_keywords:
            return True
        return False


class Select(Component):
    keyword_order = ['SELECT', 'FROM', 'JOIN', 'WHERE', 'ORDER BY']

    def __init__(self, component_string):
        super().__init__(component_string)
        if component_string[0] == '(':
            self.sql = self.sql[1:-1]

    def generate_response(self):
        components = []
        moving_sql = self.sql
        component_string = get_string_between_substrings(moving_sql, 'SELECT',
                                                         'FROM')
        moving_sql = get_string_after_substring(moving_sql, component_string)
        components.append(ColumnList(component_string, True))
        component_string = get_next_section(moving_sql, 'FROM', ['JOIN',
                                                                 'WHERE',
                                                                 'ORDER BY'])

        if component_string[0] == '(':
            components.append(Select(component_string))
        else:
            components.append(TableName(component_string))

        for component in components:
            component.check_validity()

        for component in components:
            if component.response is None:
                self.response = Response(
                    'Critical Failure: I didn\'t finish?', 1)
            elif component.response != Response.okay():
                self.response = component.response
        if self.response is None:
            self.response = Response.okay()

        # get next keyword

        pass


class Insert(Query):
    def check_query(self):
        pass


class With(Query):
    def check_query(self):
        pass

# SELECT QUERY:
# SELECT (comma separated columns or *)
# FROM (table)
# JOIN (table) ON (conditional)
# WHERE (conditional)

# INSERT QUERY 1:
# INSERT INTO (table)
# (SELECT QUERY)

# INSERT QUERY 2:
# INSERT INTO (table)
# VALUES (comma separated values)

# INSERT QUERY 3:
# INSERT INTO (table)
# (comma separated columns)
# VALUES (comma separated values)

# WITH QUERIES:
# WITH (alias) AS (SELECT QUERY)
# , (alias) AS (SELECT QUERY)
# , (SELECT QUERY)
