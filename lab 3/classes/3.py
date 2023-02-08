
# Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectange(Shape):
    def __init__(self, l, w):
        super().__init__()
        self.l = length
        self.w = width

    def area(self):
        print(self.l * self.w)


rect = Rectange(2,3)
rect.area()