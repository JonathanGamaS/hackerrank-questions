"""
One line of input containing the space separated floating number values of the X, Y and Z coordinates of a point.
Output the angle correct up to two decimal places.
"""
import math


class Points:
    def __init__(self,a,b,c):
        self.point=[a,b,c]
    def __sub__(self,other):
        return Points(*[self.point[i]-other.point[i] for i in range(3)])
    def cross(self,other):
        l=[]
        for i in range(3):
            l.append(self.point[i]*other.point[(i+1)%3]-self.point[(i+1)%3]*other.point[i])
        l[0],l[1],l[2]=l[1],l[2],l[0]
        return Points(*l)

    def dot(self,other):
        return sum([self.point[i]*other.point[i] for i in range(3)])
    def absolute(self):
        return math.sqrt(sum(map(lambda x:x**2,self.point)))

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))