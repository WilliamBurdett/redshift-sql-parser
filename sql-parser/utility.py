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
