class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.x + other.y)

    @classmethod
    def zero(cls):
        cls(0, 0)  # cls = reference of existing class

    def draw(self):  # instance method
        print(f"draw ({self.x,self.y})")


point = Point(1, 2)
# point.default_color #Class Attribute
# point.z = 10  # instanceAttributes
point.draw()
