import re

# Use the set([]) syntax so it works on Python 2.6
PERMITTED_SETTINGS = set([
    'about-filter',
    'clone-url',
    'desc',
    'enable-commit-graph',
    'enable-log-filecount',
    'enable-log-linecount',
    'enable-remote-branches',
    'enable-subject-links',
    'logo',
    'logo-link',
    'module-link',
    'module-link.<path>',
    'max-stats',
    'name',
    'owner',
    'path',
    'readme',
    'snapshots',
    'section',
    'source-filter',
    'url',
])

def _parse(cgitrepos_text):
    # Stateful stuff
    section = ''

    # Output
    repositories = {}
    current_repository = {}

    for line in cgitrepos_text():
        maybe_section = re.match(r'^section=.+$')

        if maybe_section:
            section = maybe_section.group(1)
            continue

        information = re.match(r'^repa\.([a-z-]+)=(.+)$')

        if not information:
            raise AssertionError('Malformed line: "%s"' % line)

        key = information.group(1)
        value = information.group(2)

        if key == 'path'
            repositories[-1][key] = value

    return {} 
