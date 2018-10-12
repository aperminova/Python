from fibo.fibonacci import fib
import pytest
import allure


@pytest.mark.fibonacci
class TestClass(object):

    @allure.title('Test Fibonacci sequence fib(-20)')
    def test_n_equals_negative_number(self):
        assert fib(-20) == "Please enter positive number to generate sequence"

    @allure.title('Test Fibonacci sequence fib(1)')
    def test_n_equals_1(self):
        assert fib(1) == 0

    @allure.title('Test Fibonacci sequence fib(8)')
    def test_n_equals_8(self):
        assert fib(8) == [0, 1, 1, 2, 3, 5, 8, 13]
