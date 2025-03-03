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
