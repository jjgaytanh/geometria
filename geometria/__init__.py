class TrianguloRectangulo:
    """ This class represents a right triangle of sides 'x' and 'y' with hypotenuse 'h';
        and helps with the calculation of its area and perimeter.
        Also, being 'phi' the angle formed between 'x' and 'h', the sine, cosine and
        tangent of 'phi' can be calculated as well with their correspondant methods.

    """
    def __init__(self, x=None, y=None):
        if x is None:
            self.x = float(input("X: "))
        else:
            self.x = x
        if y is None:
            self.y = float(input("Y: "))
        else:
            self.y = y
        self.h = self.hipotenusa()
    def hipotenusa(self):
        """ Return the hypotenuse of the triangle, calculated as:
            h = sqrt(x^2 + y^2)
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def area(self):
        """ Return the area of the triangle, calculated as:
            area = (x * y)/2
        """
        return (self.x * self.y) / 2
    def perimetro(self):
        """ Return the perimeter of the triangle, calculated as:
            perimeter = x + y + h
        """
        return (self.x + self.y + self.h)
    def sin(self):
        """ Being 'phi' the angle between x and h, this function
            returns the sine of phi calculated as:
            sin(phi) = y/h
        """
        return self.y / self.h
    def cos(self):
        """ Being 'phi' the angle between x and h, this function
            returns the cosine of phi calculated as:
            cos(phi) = x/h
        """
        return self.x / self.h
    def tan(self):
        """ Being 'phi' the angle between x and h, this function
            returns the tangent of phi calculated as:
            tan(phi) = y/x
        """
        return self.y / self.x

class Rectangulo:
    """ This class represents a rectangle of sides 'x' and 'y';
        and helps with the calculation of its area, perimeter and diagonal.
    """
    def __init__(self, x=None, y=None):
        if x is None:
            self.x = float(input("X: "))
        else:
            self.x = x
        if y is None:
            self.y = float(input("Y: "))
        else:
            self.y = y
    def area(self):
        """ Return the area of the rectangle, calculated as:
            area = x * y
        """
        return self.x * self.y
    def perimetro(self):
        """ Return the perimeter of the rectangle, calculated as:
            perimeter = 2(x + y)
        """
        return (self.x + self.y) * 2
    def diagonal(self):
        """ Return the diagonal of the rectangle, calculated as:
            d = [(x^2 +  y^2)] ^ (1/2)
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

class Cuadrado:
    """ This class represents a square of side 'x';
        and helps with the calculation of its area, perimeter and diagonal.
    """
    def __init__(self, x=None):
        if x is None:
            self.x = float(input("X: "))
        else:
            self.x = x
    def area(self):
        """ Return the area of the square, calculated as:
            area = x^2
        """
        return self.x * self.x
    def perimetro(self):
        """ Return the perimeter of the square, calculated as:
            perimeter = 4(x)
        """
        return self.x * 4
    def diagonal(self):
        """ Return the diagonal of the square, calculated as:
            d = [2(x^2)] ^ (1/2)
        """
        return (self.x ** 2 + self.x ** 2) ** 0.5

class Circulo:
    """ This class represents a circle of radius 'r' and diameter 'd';
        and helps with the calculation of its area and perimeter.
    """
    def __init__(self, r=None):
        if r is None:
            self.r = float(input("r: "))
        else:
            self.r = r
        self.d = 2 * self.r
    def area(self):
        """ Return the area of the circle, calculated as:
            area = pi(r^2)
        """
        import math
        return math.pi * self.r ** 2
    def perimetro(self):
        """ Return the perimeter of the circle, calculated as:
            perimeter = pi(2r)
        """
        import math
        return math.pi * self.r * 2

class Cilindro(Circulo):
    """ This class represents a cilinder of radius 'r' and height 'h';
        and helps with the calculation of its area, perimeter and volume.
    """
    def __init__(self, r=None, h=None):
        if r is None:
            self.r = float(input("r: "))
        else:
            self.r = r
        self.d = 2 * self.r
        if h is None:
            self.h = float(input("h: "))
        else:
            self.h = h
    def area_tapa(self):
        """ Return the area of the circle, calculated as:
            area = pi(r^2)
        """
        return Circulo.area(self)
    def perimetro(self):
        """ Return the perimeter of the circle, calculated as:
            perimeter = pi(2r)
        """
        return Circulo.perimetro(self)
    def area(self):
        """ Return twice the area of the circle (pi*r^2), plus the
            area of the body of the cilinder (2pi*r*h)
        """
        return 2 * self.area_tapa() + self.h * self.perimetro()
    def volumen(self):
        """ Return the volume of the cilinder calculated as
            (pi*r^2)*h
        """
        return self.area_tapa() * self.h

