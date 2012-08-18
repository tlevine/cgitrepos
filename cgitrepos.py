import re

def _parse(cgitrepos_text):
    for row in cgitrepos_text():
        assert re.match(r'^repo\.[a-z-]
