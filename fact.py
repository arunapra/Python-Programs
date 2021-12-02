

class A:
    v=100

    @classmethod
    def getv(cls):
        cls.v=50
        return cls.v

    @staticmethod
    def simple():
        print("Hi")


a=A()
print(A.getv())
A.v=30
print(A.v)
A.simple()
