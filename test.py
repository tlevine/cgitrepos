import os
import re
import json
import nose.tools as n
import nose
from cgitrepos import _parse

def _check_fixture(name):
    "Check a cgitrepos file in the fixtures directory."
    cgitrepos = open(os.path.join('fixtures', name))
    cgitrepos_json = open(os.path.join('fixtures', name + '.json'))

    # Check that the cgitrepos file matches the JSON.
    try:
        observed = _parse(cgitrepos.read())
    except:
        # Such a hack
        observed = []

    expected = json.dumps(cgitrepos_json.read())

    if type(observed) != list:
        # Point out that the JSON file is bad.
        assert 'The test is malformed; the file %s must be a list at its root.'

    elif type(expected) != list:
        # Point out that lists aren't being generated
        n.assert_list_equal(observed, expected)

    else:
        # Test each contained list (section) and associative array (repository).
        for section_or_repo in expected:
            if type(section_or_repo) == list:
                # It's a section
                pass

            elif type(section_or_repo) == dict:
                # It's a repository
                pass

            else:
               assert 'Sections (lists) in the JSON file may only contain repositories (associative arrays).'

        # Actually, that's too hard.
        n.assert_list_equal(observed, expected)

    cgitrepos.close()
    cgitrepos_json.close()

# Define tests for each thing in the fixtures directory.
fixtures = set()
for name in os.listdir('fixtures'):
    cgitrepos_file = re.match('^(.*)\.json$', name)
    if cgitrepos_file:
        fixtures.add(cgitrepos_file.group(1))

# Now the variable "fixtures" contains the names.
def test_fixture():
    "Run tests for all fixtures."
    for fixture in fixtures:
        yield _check_fixture, fixture

nose.main()
