class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        cls(0, 0)  # cls = reference of existing class

    def draw(self):  # instance method
        print(f"draw ({self.x,self.y})")


point = Point(1, 2)
# point.default_color #Class Attribute
# point.z = 10  # instanceAttributes
point.draw()
