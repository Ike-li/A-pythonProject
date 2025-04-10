class A:
    def __init__(self):
        print("A init")


class B(A):
    def __init__(self):
        super().__init__()
        print("B init")


class C(A):
    def __init__(self):
        super().__init__()
        print("C init")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")


d = D()
print(D.__mro__)


"""
A init
C init
B init
D init
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""
