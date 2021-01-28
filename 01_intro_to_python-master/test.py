import unittest
from main import *


class TestSquareTestCase(unittest.TestCase):
    def test_square_functionality(self):
        self.assertEqual(2**2, square(2))

    def test_square_output_type(self):
        self.assertEqual(type(square(2)), int)


class TestIsEvenTestCase(unittest.TestCase):
    def test_is_even_functionality(self):
        self.assertEqual(True, is_even(x=2))
        self.assertEqual(False, is_even(x=1))

    def test_is_even_output_type(self):
        self.assertEqual(bool, type(is_even(x=2)))


class TestMaximumTestCase(unittest.TestCase):
    def test_maximum_functionality(self):
        idx, val = maximum(x=[1.0, 2.0, 3.0])
        self.assertEqual(3.0, val)
        self.assertEqual(2, idx)

        idx, val = maximum(x=[3.0, 2.0, 1.0])
        self.assertEqual(3.0, val)
        self.assertEqual(0, idx)

    def test_maximum_output_type(self):
        idx, val = maximum(x=[1.0, 2.0, 3.0])
        self.assertEqual(int, type(idx))
        self.assertEqual(float, type(val))


class TestFibonacciTestCase(unittest.TestCase):
    def test_fibonacci_functionality(self):
        self.assertEqual(2, fib(2))
        self.assertEqual(3, fib(3))
        self.assertEqual(5, fib(4))
        self.assertEqual(8, fib(5))
        self.assertEqual(13, fib(6))

    def test_fibonacci_output_type(self):
        self.assertEqual(int, type(fib(3)))


class TestDotProductTestCase(unittest.TestCase):
    def test_dot_product_functionality(self):
        self.assertAlmostEqual(2.0, dot_product(x=[1.0, 1.0], y=[1.0, 1.0]))

    def test_dot_product_output_type(self):
        self.assertEqual(float, type(dot_product(x=[1.0, 1.0], y=[1.0, 1.0])))


class TestConvolutionTestCase(unittest.TestCase):
    def test_convolution_functionality(self):
        self.assertEqual([1.0, 2.0, 1.0], convolve(x=[1.0, 1.0], y=[1.0, 1.0]))
        self.assertEqual([1.0, 2.0, 3.0, 2.0, 1.0], convolve(x=[1.0, 1.0, 1.0], y=[1.0, 1.0, 1.0]))
        self.assertEqual([1.0, 3.0, 3.0, 2.0], convolve(x=[1.0, 2.0], y=[1.0, 1.0, 1.0]))
        self.assertEqual([1.0, 3.0, 3.0, 2.0], convolve(x=[1.0, 1.0, 1.0], y=[1.0, 2.0]))

    def test_convolution_output_type(self):
        self.assertEqual(list, type(convolve(x=[1.0, 1.0], y=[1.0, 1.0])))
