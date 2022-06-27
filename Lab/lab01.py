def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    times = 0
    product = 1
    while times < k:
        if k > 0:
            product *= (n - times)
            times += 1
        else:
            return product
    return product


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    power = 1
    digit = 0
    sum = 0
    while y // power != 0 :
        digit = (y % (power * 10)) // power
        sum += int(digit)
        power *= 10
        #print("Debug: digit =",digit)
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    power = 1
    sum = 0
    while n // power != 0:
        digit = (n % (power * 10)) // power
        power *= 10
        if digit == 8:
            sum += 1
    #print("Debug: how many eights =",sum)
    if sum >= 2:
        return True
    else:
        return False
