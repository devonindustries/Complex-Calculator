import math

class Complex:
    '''
    A class for defining complex numbers.
    '''

    #----------------
    # Initiation Function
    #----------------

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    #----------------
    # Built-in Arithmetic Operations
    #----------------

    def __add__(self, other):

        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __sub__(self, other):

        return Complex(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    def __mul__(self, other):

        return Complex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __truediv__(self, other):

        d = other.real ** 2 + other.imaginary ** 2

        return Complex(
            (self.real * other.real + self.imaginary * other.imaginary) / d,
            (self.imaginary * other.real - self.real * other.imaginary) / d
        )

    #----------------
    # Comparison Operations
    #----------------

    # Equality
    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        else:
            return False

    # Non Equality
    def __ne__(self, other):
        return not(self == other)

    # Less Than
    def __lt__(self, other):
        if abs(self) < abs(other):
            return True
        else:
            return False

    # Less Than / Equal
    def __le__(self, other):
        return (self == other or self < other)

    # Greater Than
    def __ge__(self, other):
        if abs(self) > abs(other):
            return True
        else:
            return False

    # Greater Than / Equal
    def __gt__(self, other):
        return (self == other or self > other)


    #----------------
    # Position & Negation
    #----------------

    def __pos__(self):

        return self

    def __neg__(self):

        return Complex(-1, 0) * self

    #----------------
    # Numerical Functions
    #----------------

    def __abs__(self):

        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def __invert__(self):
        
        return Complex(1,0) / self

    def __pow__(self, power):

        if type(power) == int:
            
            if power == 0:
                return 1
            elif power > 0:
                res = self
                for i in range(1, power):
                    res *= self
            else:
                res = Complex(1,0) / self
                for i in range(-1, power, -1):
                    res *= Complex(1,0) / self

        return res
    
    #----------------
    # Type Conversion
    #----------------

    def __str__(self):

        re_str = ""
        im_str = ""

        if self.real > 0 or self.real < 0:
            re_str = str(self.real)

        if self.imaginary > 0 and self.real != 0:
            im_str = "+" + str(self.imaginary) + "i"
        elif self.imaginary > 0 or self.imaginary < 0:
            im_str = str(self.imaginary) + "i"

        return re_str + im_str

    #----------------
    # Complex Methods
    #----------------

    def arg(self):
        '''
        Returns the argument of a complex number
        '''
        if self.real == 0:
            if self.imaginary == 0:
                return 0
            elif self.imaginary > 0:
                return math.pi / 2
            else:
                return -math.pi / 2

        elif self.real > 0:
            if self.imaginary == 0:
                return 0
            else:
                return math.atan(self.imaginary / self.real)

        else:
            if self.imaginary == 0:
                return math.pi
            elif self.imaginary > 0:
                return math.atan(abs(self.real / self.imaginary)) + math.pi / 2
            else:
                return -math.atan(abs(self.imaginary / self.real)) - math.pi / 2

    def conjugate(self):
        '''
        Returns the conjugate of the complex number
        '''
        return Complex(
            self.real,
            -1 * self.imaginary
        )

    def mod_arg(self):
        '''
        Returns a tuple containing the modulus and argument of the complex number respectively.
        '''
        return (
            abs(self),
            self.arg()
        )