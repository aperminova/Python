from phase1.fibonacci import fib


class TestClass(object):

    def test_n_equals_negative_number(self):
        assert fib(-20) == "Please enter positive number to generate sequence"

    def test_n_equals_1(self):
        assert fib(1) == 0

    def test_n_equals_8(self):
        assert fib(8) == [0, 1, 1, 2, 3, 5, 8, 13]
