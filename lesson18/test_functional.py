from lesson18.code_for_test18 import Human
import pytest

@pytest.mark.xfail(reason= "failed due to know bug @72137213721")
def test_change_hair_color():
    human = Human('Alnert', 8, 'pink')
    human.change_color('black')
    assert human.color == 'black'


@pytest.mark.smoke
@pytest.mark.skip("this test would be skipped")
def test_age_growth(human):
    human.grow()
    assert human.age == 26

@pytest.mark.regression
def test_age_growth(human):
    human.grow()
    assert human.age == 26
