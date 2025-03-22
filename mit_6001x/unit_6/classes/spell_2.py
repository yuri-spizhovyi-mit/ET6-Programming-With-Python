class A:
    def __init__(self):
        print("A.__init__")
        self.a = 1


class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()
        self.a = 2
        self.b = 3


class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()
        # self.a = 4
        self.c = 5


class D(C, B):
    def __init__(self):
        print("D.__init__")
        super().__init__()
        self.d = 6


obj = D()
print(obj.a)
