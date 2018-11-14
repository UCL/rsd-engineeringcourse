import yaml
import os
import pytest
from ..greeter import greet

def read_fixture():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures',
                           'samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
    return fixtures

@pytest.mark.parametrize("fixture", read_fixture())
def test_greeter(fixture):
    answer = fixture.pop('answer')
    assert greet(**fixture) == answer