from sql_parser.reponse import Response


def get_string_between_substrings(string, first, last):
    try:
        start = string.index(first) + len(first)
        end = string.index(last, start)
        return string[start:end]
    except ValueError:
        return ""


def remove_all_whitespace_characters(string):
    return ''.join(string.split())


def get_string_after_substring(string, substring):
    try:
        string = string[string.index(substring) + len(substring):]
        return string
    except ValueError:
        return ""


def spaces_encased_by_quotes(string):
    removed_spaces = remove_all_whitespace_characters(string)
    if '"' not in string:
        if string == removed_spaces:
            return True
        return False
    return True


def check_bracket_order(conditional_section):
    bracket_stack = []
    for index, character in enumerate(conditional_section):
        if character == '(':
            bracket_stack.append(index)
        elif character == ')':
            if len(bracket_stack) == 0:
                return Response('Brackets don\' match', 1)
            bracket_stack.pop()
    if len(bracket_stack) != 0:
        return Response('Brackets don\' match', 1)
    return Response.okay()


def get_next_section(sql, current_keyword, optional_keywords):
    # we gotta be careful to keep anything in brackets as one thing
    # Check for brackets
    # If brackets, return that
    # if none, find next keyword
    sql = get_string_after_substring(sql, current_keyword)
    trimmed = sql.strip()
    if trimmed[0] == '(':
        bracket_stack = []
        for index, character in enumerate(trimmed):
            if character == '(':
                bracket_stack.append(index)
            elif character == ')':
                bracket_stack.pop()
            if len(bracket_stack) == 0:
                return trimmed[0:index + 1]
        return 1  # We opened a bracket but never closed it

    # Want the longest section left
    # Return the between start and that keyword
    section_text = ''
    keyword_string = ''
    for keyword in optional_keywords:
        rest_of_sql = get_string_after_substring(sql, keyword)
        if len(rest_of_sql) > len(keyword_string):
            keyword_string = rest_of_sql
            section_text = get_string_between_substrings(sql, '', keyword)
    if not section_text == '':
        return section_text

    return sql
