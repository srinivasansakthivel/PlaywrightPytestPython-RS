import pytest


@pytest.fixture(scope="module")
def preWork():
    print("Setup browser instance")
    return "pass"


@pytest.fixture(scope="function")
def secondWork():
    print("Setup browser instance")
    yield
    print("tear down validation")


def test_initial_check(preWork, secondWork):
    print("This is first test")
    assert preWork == "pass"


@pytest.mark.skip
def test_second_check(preSetupWork, secondWork):
    print("This is second test")
