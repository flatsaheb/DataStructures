'''
Abstract Class Concept. This can be used as template for writing code
based on abstraction.
'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def fCircleArea(self,l_Radius):
        pass
    @abstractmethod
    def fSquare(self,l_Side):
        pass
    @abstractmethod
    def fRectangle(self, l_Length, l_Breadth):
        pass
class Area(Shape):
    def fCircleArea(self,l_Radius):
        lArea = 3.14*l_Radius*l_Radius
        return lArea
    def fSquare(self,l_Side):
        lArea = l_Side*l_Side
        return lArea
    def fRectangle(self, l_Length, l_Breadth):
        lArea = l_Length*l_Breadth
        return lArea
    def fRectanglePerimeter (self,l_Length, l_Breadth):
        lPerimter = 2*l_Length*l_Breadth
        return lPerimter

OArea = Area()
print (OArea.fCircleArea(2))
print (OArea.fSquare(4))
print (OArea.fRectanglePerimeter(3,4))
print (OArea.fRectangle(3,4))