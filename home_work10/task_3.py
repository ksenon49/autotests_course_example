# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest



def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('test_input, result', [
    pytest.param((8, 2), 4, marks=pytest.mark.smoke('smoke')),
    pytest.param((2.3, 1), 2.3, marks=pytest.mark.skip('not work')),
    ((3, 0.5), 6),
    ((8, 0), ZeroDivisionError),
    ])
def test_division(*test_input, result):
    try:
        assert all_division(*test_input) == result
    except ZeroDivisionError as error:
        assert error

