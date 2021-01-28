from typing import Sequence, Tuple



def square(x: int) -> int:
    """ Square the input argument

    Args:
        x (int): number to square

    Returns:
        val (int): squared value of x
    """
    return x * x


def is_even(x: int) -> bool:
    """ Determine whether a number is even or not

    Args:
        x (int): number to determine parity

    Returns:
        even (bool): True if x is is even
    """
    if x % 2 == 0:
        return True

    return False


def fib(n: int) -> int:
    """ Returns the nth value of the Fibonacci sequence defined by:

    x_n = x_{n - 1} + x_{n - 2}

    where x_0 and x_1 are explicitly defined as 1

    Args:
        n (int): index of the fibonacci sequence to return

    Returns:
        val (int): nth value in the fibonacci sequence
    """

    # 1 has to be returned since x_0 and x_1 are explicitly defined as 1
    if n <= 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def maximum(x: Sequence[float]) -> Tuple[int, float]:
    """ Find the maximum element in a vector and return its index and value

    Args:
        x (sequence): sequence representing a vector of floats

    Notes:
        When the maximum value is duplicated in the sequence, return the first index.

    Returns:
        index (int): index at which maximum is found
        value (float): maximum value in the vector
    """

    max_val = max(x)
    index = x.index(max_val)

    return index, max_val


def dot_product(x: Sequence[float], y: Sequence[float]) -> float:
    """ A dot product of two vectors x and y is defined as the sum of the products
    of all elements of x and y

    Args:
        x (sequence): sequence representing a vector of floats
        y (sequence): sequence representing a vector of floats

    Notes:
        Sequences in Python are guaranteed for len([var_name]) to return a length

    Raises:
        ValueError: if len(x) != len(y)

    Returns:
        dot_product (float): dot product of x and y
    """

    if len(x) != len(y):
        raise ValueError

    product_x = 1
    product_y = 1
    i = 0

    while i < len(x):
        product_x *= x[i]
        product_y *= y[i]
        i += 1

    return product_x + product_y


def convolve(x: Sequence[float], y: Sequence[float]) -> Sequence[float]:
    """ A FULL convolution of a vector x of length N and a vector y of length M is defined as
        the summation:

        sum_{m} x[m]*y[n - m].

        There will be N + M - 1 meaningful outputs of this summation given the lengths of x and y

    Args:
        x (sequence): sequence representing a vector of floats
        y (sequence): sequence representing a vector of floats

    Notes:
        DO NOT use an external library to complete this function.

        A reference implementation in C++ can be found:
        https://stackoverflow.com/questions/24518989/how-to-perform-1-dimensional-valid-convolution

    Returns:
        convolution (sequence): convolution product of x and y
    """
    x_len = len(x)
    y_len = len(y)

    n = x_len + y_len - 1

    # Make an empty list of length n
    result = [0] * n

    for i in range(n):
        jmn = i - (y_len - 1) if (i >= y_len - 1) else 0
        jmx = i if (i < x_len - 1) else (x_len - 1)

        for j in range(jmn, jmx+1):
            result[i] += (x[j] * y[i - j])

    return result
