'''
Operator Overloading. In this program we are using __mul__ operator to overload to
multiply values of two objects.
'''

class Shapes:

    def __init__(self, l_Lenght, l_Breadth):
        self.lLenght = l_Lenght
        self.lBreadth = l_Breadth

    def __mul__(self, other):
        lLength1 = self.lLenght * other.lLenght
        lBreadth1 = self.lBreadth * other.lBreadth
        lTotalLen = Shapes(lLength1, lBreadth1)
        return lTotalLen

    def __gt__(self, other):
        lLength2 = self.lLenght * self.lBreadth
        lBreadth2 = other.lBreadth * other.lLenght
        if lLength2 > lBreadth2:
            return True
        else:
            return False

s1 = Shapes(5,10)
s2 = Shapes(8,7)

# 8 * 5 & 10 * 7
s3 = s1*s2
print(s3.lLenght)
print(s3.lBreadth)

if s1 > s2:
    print ('S1 longer')
else:
    print ('S2 longer')