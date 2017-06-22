from .component import Component
from .utility import spaces_encased_by_quotes, get_string_between_substrings
from .reponse import Response


class TableName(Component):
    def __init__(self, component_string):
        super().__init__(component_string)
        self.trimmed = self.sql.strip()
        self.schema = None
        self.table = None
        self.alias = None

    def generate_response(self):
        self.set_schema()
        self.set_alias_name()
        self.set_table_name()

        if self.table is None or self.table == '':
            self.response = Response('Failed to parse Table Name', 1)
            return
        # check each field for space/quote
        if self.schema:
            if not spaces_encased_by_quotes(self.schema):
                self.response = Response(
                    'Schema Name has spaces without quotes', 1)
                return
            if not self.schema.count('"') == 2 and self.schema.count('.') == 1:
                self.response = Response(
                    'Schema Name has period without quotes', 1)
                return
            if self.sql.split(self.schema)[1][0] != '.':
                self.response = Response('No period proceeding Schema Name', 1)
                return
        if self.alias:
            if not spaces_encased_by_quotes(self.alias):
                self.response = Response('Alias has spaces without quotes', 1)
                return
            if not get_string_between_substrings(self.sql, self.table,
                                                 self.alias).isspace():
                self.response = Response('No space between alias and table', 1)
                return
        if not spaces_encased_by_quotes(self.table):
            self.response = Response('Table Name has spaces without quotes', 1)
            return
        self.response = Response.okay()

    def set_table_name(self):
        table = self.sql
        if self.schema:
            table = table.split(self.schema)[1][1:]
        if self.alias:
            table = table.split(self.alias)[0][:-1]
        self.table = table.strip()

    def set_schema(self):
        if self.trimmed.count('.') > 1:
            parts = self.trimmed.split('.')
            self.schema = parts[0] + '.' + parts[1]
            self.schema = self.schema.strip()
        elif self.trimmed.count('.') == 1:
            parts = self.trimmed.split('.')
            self.schema = parts[0]
            self.schema = self.schema.strip()

    def set_alias_name(self):
        if self.schema:
            # Splitting on schema then excluding the proceeding period
            table_and_alias = self.trimmed.split(self.schema)[1][1:]
        else:
            table_and_alias = self.trimmed

        if table_and_alias.count('"') == 0:
            parts = table_and_alias.split(" ")
            if len(parts) > 2:
                self.response = Response(
                    'Too many words near the Table Name and Alias', 1)
            elif len(parts) == 2:
                self.alias = parts[1]
                # If it is 1, then that's the table name.
                # Setting in it's own method for ease
        elif table_and_alias.count('"') == 2:
            # one of them has quotes
            # Check to see if
            if not spaces_encased_by_quotes(table_and_alias):
                split = table_and_alias.split('"')
                if split[0] == '' and not split[2] == '':
                    # table name is in quotes
                    # alias is after
                    if not split[2][0].isspace():
                        self.response = Response(
                            'No space between Table Name and Alias', 1)
                    else:
                        self.alias = split[2]
                else:
                    self.alias = '"' + split[1] + '"'
        elif table_and_alias.count('"') == 4:
            self.alias = '"' + table_and_alias.split('"')[3] + '"'
        else:
            # Odd or too many quotes
            self.response = Response(
                'Odd number or too many quotes around the Table Name', 1)
