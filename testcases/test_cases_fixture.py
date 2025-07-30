
import pytest

@pytest.fixture()
def fixture_code():
    print("this is code execute before test case execution")
    yield
    print("this is code execute after test case execution")

@pytest.mark.first
def test_first_test_case(fixture_code):
    print("this is first test case")

@pytest.mark.first
def test_second_test_case(fixture_code):
    print("this is second test case")


