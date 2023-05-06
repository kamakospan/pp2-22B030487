# 4. Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

p1 = Point(1, 2)
p2 = Point(2, 3)
p1.get_coordinates()
p2.get_coordinates()
print(p1.dist(p2))
p1.move(2, 2)
p1.get_coordinates()