# Write a Python program to insert spaces between words starting with capital letters.

import re
text = "IHadNoSpacesButThisProgramMadeMeHaveSpaces"

changed_string = re.findall(r"[A-Z][a-z]*", text)
print(' '.join(changed_string))