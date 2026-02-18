import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("Setup browser instance - session scope")

