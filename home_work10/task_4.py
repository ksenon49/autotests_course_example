# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
from test_task102 import all_division

class TestClass:


    @pytest.mark.usefixtures('start_time')
    @pytest.mark.parametrize('args, result', [pytest.param([8, 2], 4, marks=pytest.mark.smoke),
                                              pytest.param([3, 0.5], 6)])
    def test1(self, args, result):
        assert all_division(*args) == result

    @pytest.mark.usefixtures('run_time')
    @pytest.mark.parametrize('args, result', [pytest.param([2, 5, 1], 0.4),
                                              pytest.param([2.3, 1], 2.3, marks=pytest.mark.skip('not work'))])
    def test2(self, args, result):
        assert all_division(*args) == result
