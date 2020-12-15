from typing import Union
import numpy as np


class MyVector():
    def __init__(self, dimension, *args: Union[int, float]):
        self.__dimension: int = dimension
        self.__args: np.array[Union[int, float]] = np.array(args)

    def __str__(self):
        string = '(' + ", ".join(map(str, self.__args)) + ')'
        return string

    def __neg__(self):
        self.__args = np.array(list(map(lambda x: -x, self.__args)))
        return self

    def __repr__(self):
        string = 'MyVector(' + ', '.join(map(str, self.__args)) + ')'
        return string

    def __mul__(self, other):
        return float(np.dot(self.__args, other.__args))

    def vector_norm(self):
        return np.linalg.norm(self.__args)

    @property
    def dimension(self):
        return self.__dimension

    def __getitem__(self, coord):
        return self.__args[coord]

    def __setitem__(self, key, value):
        assert (isinstance(value, int) or isinstance(value, float))
        self.__args[key] = value

    def __len__(self):
        return self.__dimension

    def __iadd__(self, other):
        self.__args += other.__args
        return self

    def __add__(self, other):
        sum_coords = self.__args + other.__args
        return MyVector(self.dimension, *sum_coords)

    def __sub__(self, other):
        sum_coords = self.__args - other.__args
        return MyVector(self.dimension, *sum_coords)

    def __isub__(self, other):
        self.__args -= other.__args
        return self

    def __eq__(self, other):
        return self.__args == other.__args

    def __lt__(self, other):
        return self.vector_norm() < other.vector_norm()

    def __ge__(self, other):
        return self.vector_norm() >= other.vector_norm()


if __name__ == '__main__':
    N = int(input())
    dim_and_coords = list(map(float, input().split()))
    dimension = dim_and_coords[0]
    vector_list = [MyVector(*dim_and_coords)]

    for i in range(N - 1):
        flag = False
        while not flag:
            dim_and_coords = list(map(float, input().split()))
            if len(dim_and_coords) - 1 != dimension:
                raise ValueError("enter the vector".
                                 format(dimension))
            else:
                vector_list.append(MyVector(*dim_and_coords))
                flag = True

    max_distance = 0
    max_vector = None
    for vector in vector_list:
        if max_distance < vector.vector_norm():
            max_distance = vector.vector_norm()
            max_vector = vector

    print("maximum, when compared norm value: ", repr(max_vector))

    print("running through the vector by iterations")
    vector = MyVector(5, 1, 2, 3, 4, 4)
    for i in range(len(vector)):
        print(vector[i])

    vector_1 = MyVector(3, 1, 100, 1)
    vector_2 = MyVector(3, 0, 1, 0)
    print("result of a dot product", vector_1 * vector_2)

    print("sum of the vectors: ", MyVector(2, 1, 1) + MyVector(2, 4, 5))
    print("Euclidean norm: ", (MyVector(4, 1, 2, 3, 4).vector_norm()))
    print("opposite vector: ", -vector_1)

