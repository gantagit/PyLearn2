# Automation from Scratch
import pytest
import allure


@allure.title("TC1 - Sanity Check")
@allure.description("Test cases to verify 2+2==4")
@pytest.mark.sanity(reason="This is a sanity test")
def test_add1():
    assert 2 + 2 == 4


@allure.title("TC2 - regression tests")
@allure.description("Test cases to verify 2/1==")
@pytest.mark.regression(reason="This is a regression test")
def test_div1():
    assert 2 / 1 == 1


@allure.title("TC3 - smoke tests")
@allure.description("Test cases to 2+2==4")
@pytest.mark.smoke(reason="This is a smoke test")
def test_add2():
    assert 2 + 2 == 4

@allure.title("TC4 - skip tests")
@allure.description("Test cases to 2+2==-4")
@pytest.mark.skip(reason="This is a not working test")
def test_add3():
    assert 2 + 2 == -4


@allure.title("TC5 - smoke tests")
@allure.description("Test cases to 2/1==2")
@pytest.mark.smoke(reason="This is a smoke test")
def test_div3():
    assert 2 / 1 == 2
