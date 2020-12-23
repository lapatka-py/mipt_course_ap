class Shape():
    def __init__(self, number_1, number_2):
        self.height = int(number_1)
        self.wide = int(number_2)


class Triangle(Shape):
    def area(self):
        return 0.5 * self.height * self.wide


class Rectangle(Shape):
    def area(self):
        return self.height * self.wide


area1 = Triangle(5, 5)
area2 = Rectangle(5, 5)

print(area1.area())
print(area2.area())
