from .component import Component
from .utility import spaces_encased_by_quotes, get_string_between_substrings


class TableName(Component):
    def __init__(self, component_string):
        super().__init__(component_string)
        self.trimmed = self.sql
        self.schema = None
        self.table = None
        self.alias = None

    def check_validity(self):
        self.set_schema()
        self.set_alias_name()
        self.set_table_name()

        # check each field for space/quote
        if self.schema:
            if not spaces_encased_by_quotes(self.schema):
                self.is_valid = False
                return 1
            if not self.schema.count('"') == 2 and self.schema.count('.') == 1:
                self.is_valid = False
                return 1
            if self.sql.split(self.schema)[1][0] != '.':
                self.is_valid = False
                return 1
        if self.alias:
            if not spaces_encased_by_quotes(self.alias):
                self.is_valid = False
                return 1
            if not get_string_between_substrings(self.sql, self.table,
                                                 self.alias).isspace():
                self.is_valid = False
                return 1
        if not spaces_encased_by_quotes(self.table):
            self.is_valid = False
            return 1

        self.is_valid = True
        return 0

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
                self.is_valid = False
                return 1
            if len(parts) == 2:
                self.alias = parts[1]
                # If it is 1, then that's the able name.
                # Setting in it's own method for ease
        if table_and_alias.count('"') == 2:
            # one of them has quotes
            # Check to see if
            space_outside_quotes = spaces_encased_by_quotes(table_and_alias)
            if space_outside_quotes:
                return 0
            else:
                split = table_and_alias.split('"')
                if split[0] == '' and split[2] == '':
                    # table name is in quotes
                    # no alias
                    return 0
                elif split[0] == '' and not split[2] == '':
                    # table name is in quotes
                    # alias is after
                    if not split[2][0].isspace():
                        self.is_valid = False
                        return 1
                    self.alias = split[2]
                    return 0
                self.alias = '"' + split[1] + '"'
                return 0
        if table_and_alias.count('"') == 4:
            self.alias = '"' + table_and_alias.split('"')[3] + '"'
            return 0
        else:
            self.is_valid = False
            return 1  # Odd number or too many
