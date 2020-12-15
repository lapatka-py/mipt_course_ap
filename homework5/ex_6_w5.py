class Animal():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description


class Zebra(Animal):
    __legs = 4

    def __init__(self, name, age, legs):
        super().__init__(name, age)
        self.__legs = legs

    def get_legs(self):
        return self.__legs

    def get_str(self):
        return f"Name: {self.get_name()}; Age: {self.get_age()}; \
                        N of legs: {self.get_legs()}\n---"

class Dolphin(Animal):
    def get_str(self):
        return f"Name: {self.get_name()}; Age: {self.get_age()};\n---"

    def swiming(self):
        print('just swimming')

