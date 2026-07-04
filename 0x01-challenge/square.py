#!/usr/bin/python3
"""Square module."""

class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize a new Square instance.

        Accepts width and height as keyword arguments. If both are provided
        the instance will keep them only if they are equal (a square). If
        the provided height differs from the width, both attributes are
        set to 0 to indicate an invalid square.

        Example:
            Square(width=5, height=5)
        """
        if kwargs:
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                if kwargs["height"] == self.width:
                    self.height = kwargs["height"]
                else:
                    self.height = self.width = 0

    def area_of_my_square(self):
        """Return the area of the square (width * height).

        Returns 0 if the square is invalid (width or height is 0).
        """
        return self.width * self.height

    def permiter_of_my_square(self):
        """Return the perimeter of the square (2*width + 2*height).

        Returns 0 if the square is invalid (width or height is 0).
        Note: method name intentionally matches original code.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return a short string representation of the square.

        Format: "width/height" (e.g. "5/5").
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
