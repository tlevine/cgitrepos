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
        observed = {}

    expected = json.loads(cgitrepos_json.read())
    cgitrepos.close()
    cgitrepos_json.close()

    if type(expected) != dict:
        # Point out that the JSON file is bad.
        assert False, 'The test is malformed; the file %s must be a dict at its root.'

    elif type(observed) != dict:
        # Point out that the JSON file is bad.
        assert False, 'The parser returned a type other than dict.'

    else:
        # Test each associative array (repository).
        for name in expected:
            n.assert_in(name, observed)
            n.assert_dict_equal(observed[name], expected[name])

# Define tests for each thing in the fixtures directory.
fixtures = set()
for name in os.listdir('fixtures'):
    cgitrepos_file = re.match('^(.*)\.json$', name)
    if cgitrepos_file:
        fixtures.add(cgitrepos_file.group(1))

# Now the variable "fixtures" contains the names, run test for all fixtures.
def test_fixture():
    for fixture in fixtures:
        yield _check_fixture, fixture
