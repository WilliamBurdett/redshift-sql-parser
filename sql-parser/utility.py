def find_between(string, first, last):
    try:
        start = string.index(first) + len(first)
        end = string.index(last, start)
        return string[start:end]
    except ValueError:
        return ""


def remove_all_whitespace_characters(string):
    return ''.join(string.split())


def get_string_after_substring(string,  substring):
    return string[string.index(substring) + len(substring):]


def check_bracket_order(conditional_section):
    bracket_stack = []
    for index, character in enumerate(conditional_section):
        if character == '(':
            bracket_stack.append(index)
        elif character == ')':
            if len(bracket_stack) == 0:
                return 1
            bracket_stack.pop()
    if len(bracket_stack) != 0:
        return 1
    return 0
