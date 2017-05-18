# Program logic
# Get a query
# Figure out type
# Call check query on it
from query import query_factory
from parse_error import ParseError


def run_parser(sql):
    query = query_factory(sql)
    if isinstance(query, ParseError):
        print(query.message)
        return 1
    return 0