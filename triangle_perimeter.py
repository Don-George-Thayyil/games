import math


class Point:
    def __init__(self, x , y):
        self.__y = y
        self.__x = x
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
        

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        self.__sideone = ((self.__points[0].getx() - self.__points[1].getx()) ** 2 + (self.__points[0].gety() - self.__points[1].gety()) ** 2) ** 0.5 
        self.__sidetwo = ((self.__points[1].getx() - self.__points[2].getx()) ** 2 + (self.__points[1].gety() - self.__points[2].gety()) ** 2) ** 0.5 
        self.__sidethree = ((self.__points[2].getx() - self.__points[0].getx()) ** 2 + (self.__points[2].gety() - self.__points[0].gety()) ** 2) ** 0.5 
        return self.__sideone + self.__sidetwo + self.__sidethree
    
## change input here
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))
triangle = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
print(triangle.perimeter())
