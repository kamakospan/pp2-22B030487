# Write a python program to convert snake case string to camel case string.

import re
text = "i_was_written_in_a_snake_case_but_this_program_will_make_me_camel_case"

changed_string = ""
result = re.split(r"[_]",text)
for i in result:
    changed_string += i.capitalize()
print(changed_string)