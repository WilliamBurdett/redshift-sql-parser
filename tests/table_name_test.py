from sql_parser.table_name import TableName
from unittest import TestCase, main


class TestQuery(TestCase):
    def test_table_name_no_quotes(self):
        actual_input = 'table_name'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.table, 'table_name')

    def test_schema_and_table_no_quotes(self):
        actual_input = 'schema.table_name'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.schema, 'schema')
        self.assertEquals(table_name.table, 'table_name')

    def test_schema_and_table_no_quotes_alias(self):
        actual_input = 'schema.table_name alias'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.schema, 'schema')
        self.assertEquals(table_name.table, 'table_name')
        self.assertEquals(table_name.alias, 'alias')

    def test_and_table_no_quotes_alias(self):
        actual_input = 'table_name alias'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.table, 'table_name')
        self.assertEquals(table_name.alias, 'alias')

    def test_table_name_quotes(self):
        actual_input = '"table_name"'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.table, '"table_name"')

    def test_schema_and_table_quotes(self):
        actual_input = '"schema"."table_name"'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.schema, '"schema"')
        self.assertEquals(table_name.table, '"table_name"')

    def test_schema_and_table_quotes_alias(self):
        actual_input = '"schema"."table_name" "alias"'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.schema, '"schema"')
        self.assertEquals(table_name.table, '"table_name"')
        self.assertEquals(table_name.alias, '"alias"')

    def test_table_and_alias_quotes_alias(self):
        actual_input = '"table_name" "alias"'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.table, '"table_name"')
        self.assertEquals(table_name.alias, '"alias"')

    def test_too_many_periods_without_quotes(self):
        actual_input = 'sch.ema.table_name'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 1)

    def test_schema_and_table_periods_quotes(self):
        actual_input = '"sch.ema"."table_name"'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.schema, '"sch.ema"')
        self.assertEquals(table_name.table, '"table_name"')

    def test_table_alias_spaces_no_quotes(self):
        actual_input = 'table name alias'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 1)

    def test_schema_table_spaces_quotes(self):
        actual_input = '"schema"."table name"'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.schema, '"schema"')
        self.assertEquals(table_name.table, '"table name"')

    def test_schema_no_quotes_table_quotes(self):
        actual_input = 'schema."table_name"'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 0)
        self.assertEquals(table_name.schema, 'schema')
        self.assertEquals(table_name.table, '"table_name"')

    def test_space_after_period(self):
        actual_input = 'schema. table_name'
        table_name = TableName(actual_input)
        self.assertEquals(table_name.check_validity(), 1)

if __name__ == '__main__':
    main()
