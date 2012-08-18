import re

def _parse(cgitrepos_text):
    for line in cgitrepos_text():
        maybe_section = re.match(r'^section=.+$')
        if maybe_section:
            section = maybe_section.group(1)

        if not re.match(r'^repo\.[a-z-]=.+$', line):
            # Not a valid line
            continue

    return {} 
