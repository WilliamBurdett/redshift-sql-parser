# Program logic
# Get a query
# Figure out type
# Call check query on it
from .query import query_factory
from .reponse import Response


def run_parser(sql):
    response = query_factory(sql)
    if response != Response.okay():
        print(response.message)
        return response.code
    return Response.okay()


string = 'schema.table alias'
print(string[1:])
list = string.split('"')
print(list)

# list['', 'schema', '.', 'table', ' ', 'alias', '']

# 1 = schema
# 2 = period
# 3 = tablename
# 4 = alias