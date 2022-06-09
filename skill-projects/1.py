import math

import math

class obj():

    def __init__(self, __color, side=0, side_1=0, side_2=0, radius=0):
        self.__color=__color
        self.side = side
        self.side_1 = side_1
        self.side_1 = side_2
        self.radius = radius
    @property
    def a(self):
        return self.__color

    @a.setter
    def a(self,value):
        if value=='':
            self.__color = 'нет цвета'
        else:
            self.__color=str(value)

class Square(obj):

    def perimeter(self):
        return self.side*4

    def square_(self):
        return self.side**2

class rectangle(obj):

    def perimeter(self):
        return (self.side_1+self.side_2)*2

    def square_(self):
        return self.side_1*self.side_2

class circle(obj):

    def perimeter(self):
        return (2*self.radius*math.pi)*2

    def square_(self):
        return (math.pi*self.radius**2)

a=circle('red', radius=10)
print(a.square_(), a.perimeter())
b=Square('',2)
b.a='им мс'
print(b.a)




