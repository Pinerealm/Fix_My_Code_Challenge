#!/usr/bin/python3

class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize a new square object """
        if kwargs:
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                if kwargs["height"] == self.width:
                    self.height = kwargs["height"]
                else:
                    self.height = self.width = 0

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
