from typing import Union
from math import hypot


class ComplexDescriptor:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        assert (isinstance(value, int) or isinstance(value, float))

        instance.__dict__[self.__name] = value


class MyComplex:
    real = ComplexDescriptor('real')
    imag = ComplexDescriptor("imag")

    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.real = x
        self.imag = y

    def __str__(self):
        return "({}, {})".format(self.real, self.imag)

    def __repr__(self):
        return "MyComplex({}, {})".format(self.real, self.imag)

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __iadd__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self

    def __sub__(self, other):
        return MyComplex(self.real - other.real, self.imag - other.imag)

    def __isub__(self, other):
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __abs__(self):
        return hypot(self.real, self.imag)

    def __neg__(self):
        return MyComplex(-self.real, -self.imag)

    def __bool__(self):
        return self.real != 0 and self.imag != 0

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __lt__(self, other):
        return self.__abs__() < other.__abs__

    def __ge__(self, other):
        return self.__abs__() >= other.__abs__

    def __gt__(self, other):
        return self.__abs__() > other.__abs__()

    def __mul__(self, other):
        real_part_1 = self.real * other.real
        real_part_2 = -self.imag * other.imag
        complex_part_1 = self.real * other.imag
        complex_part_2 = self.real * other.imag

        return MyComplex(real_part_1 + real_part_2, complex_part_1 + complex_part_2)

    def __hash__(self):
        return hash((self.real, self.imag))


if __name__ == "__main__":
    x = MyComplex(1, 1)
    y = MyComplex(3, 3)
    print("sum of two complex numbers: ", x + y)
    print("subtraction of two complex numbers: ", x - y)
    print("absolute value", abs(x))
    print("equal or not", x == y)

