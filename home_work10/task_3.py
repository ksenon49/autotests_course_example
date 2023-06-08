# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
	

@pytest.mark.parametrize('a, b, c result', [
    pytest.param(8, 2, 4, marks=pytest.mark.smoke),
    pytest.param(2.3, 1, 2.3, marks=pytest.mark.skip('not work')),
    (3, 0.5, 6)])
def test_division(a, b, result):
    assert all_division(a, b) == result	




