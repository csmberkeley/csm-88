class A(object):
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

def test():
    """
    >>> x = A()
    >>> y = B()
    >>> x.f()
    2
    >>> B.f()
    Traceback (most recent call last):
        ...
    TypeError: f() missing 1 required positional argument: 'self'
    >>> x.g(x, 1)
    4
    >>> y.g(x, 2)
    8
    """

class Yolo:
    def __init__(self, motto):
        self.motto = motto
    def g(self, n):
        return self.motto + n

def test2():
    """
    >>> x = Yolo(1)
    >>> x.g(3)
    4
    >>> x.g(5)
    6
    >>> x.motto = 5
    >>> x.g(5)
    10
    """


