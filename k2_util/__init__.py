import string_utils as su
import re

def to_snake_case(s, separator='_'):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    if su.is_snake_case(s, separator=separator):
        return s
    return re.sub('[^a-z0-9]+', separator, s.strip().lower()).strip(separator)
    
def to_kebab_case(s):
    return to_snake_case(s, separator='-')
    
def to_camel_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    if su.is_camel_case(s):
        return s[0].lower()+s[1:]
    return su.snake_case_to_camel(re.sub('^[0-9_]+', '', to_snake_case(s)), upper_case_first=False)

def to_class_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    if su.is_camel_case(s):
        return s[0].upper()+s[1:]
    return su.snake_case_to_camel(re.sub('^[0-9_]+', '', to_snake_case(s)), upper_case_first=True)

def to_sentence_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    h = re.sub('[^a-zA-Z0-9]+', ' ', s.strip()).strip()
    return h[0].upper()+h[1:]

def to_title_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    return to_snake_case(s, separator=' ').title()

    