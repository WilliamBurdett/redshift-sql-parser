# Program logic
# Get a query
# Figure out type
# Call check query on it
from .query import query_factory
from .parse_error import ParseError


def run_parser(sql):
    query = query_factory(sql)
    if isinstance(query, ParseError):
        print(query.message)
        return 1
    return 0


string = 'schema.table alias'
print(string[1:])
list = string.split('"')
print(list)

# list['', 'schema', '.', 'table', ' ', 'alias', '']

# 1 = schema
# 2 = period
# 3 = tablename
# 4 = alias