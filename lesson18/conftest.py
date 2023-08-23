import pytest
from lesson18.code_for_test18 import Human

@pytest.fixture
def human():
    print("setup for test")
    yield  Human('Joshua', 25, 'black')
    print("teardown for test")