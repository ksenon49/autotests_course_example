# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_smoke():
    assert all_division(8, 2) == 4


@pytest.mark.zero
def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(8, 0)


def test_float1():
    assert all_division(2.3, 1) == 2.3


def test_float2():
    assert all_division(3, 0.5) == 6


@pytest.mark.acceptance
def test_negative():
    assert all_division(-20, 5) == -4
