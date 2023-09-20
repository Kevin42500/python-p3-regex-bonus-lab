import re

def match_string(input_string):
    # Regular expression for the first pattern
    pattern = r"It's such a lovely day today\."
    return bool(re.fullmatch(pattern, input_string))
