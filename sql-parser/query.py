import utility
from parse_error import ParseError
from abc import ABCMeta, abstractmethod
from reserved_keywords import reserved_keywords


def query_factory(sql):
    trimmed = sql.strip()
    if trimmed.index('SELECT') == 0:
        return Select(sql)
    elif trimmed.index('WITH') == 0:
        return With(sql)
    elif trimmed.index('INSERT') == 0:
        return Insert(sql)
    else:
        return ParseError('Failure to read query')


class Query:
    __metaclass__ = ABCMeta

    def __init__(self, query):
        self.query = query

    @abstractmethod
    def check_query(self):
        pass

    @staticmethod
    def is_reserved(string):
        if string in reserved_keywords:
            return True
        return False

    @staticmethod
    def check_sql_list(sql_list, allow_quotes = False):
        values = sql_list.split(',')
        for value in values:
            value = value.strip()
            has_whitespace = False
            if not value == utility.remove_all_whitespace_characters(value):
                has_whitespace = True
            if allow_quotes:
                if value[0] == '"' and value[-1:] == '"' and value.count('"') == 2:
                    has_whitespace = False
            if has_whitespace:
                return 1
        return 0


class Select(Query):
    def check_query(self):
        column_string = utility.find_between(self.query, 'SELECT', 'FROM')
        if len(column_string)-2 < len(column_string.strip()):
            return 1
        if not column_string.strip() == '*':
            self.check_sql_list(column_string)

        rest_of_query = utility.get_string_after_substring(self.query, 'FROM')

        return 2


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
