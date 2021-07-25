from math import *

class Complex:

    def __init__(self, Re_Part = 0, Im_Part = 0):
        self.Re = Re_Part
        self.Im = Im_Part

    def __str__(self):
        return "({}{:+}i)".format(self.Re, self.Im)

    def __repr__(self):
        return "Complex({}, {})".format(self.Re, self)
    
    def __eq__(self, sec_val):
        if self.Re == sec_val.Re and self.Im == sec_val.Im:
            return True
        return False

    def __add__(self, addend):
        sum = Complex(self.Re + addend.Re, self.Im + addend.Im)
        return sum

    def __sub__(self, subtrahend):
        difference = Complex(self.Re - subtrahend.Re, self.Im - subtrahend.Im)
        return difference

    def __mul__(self, factor):
        product_Re = self.Re * factor.Re - self.Im * factor.Im
        product_Im = self.Re * factor.Im + self.Im * factor.Re
        product = Complex(product_Re, product_Im)
        return product

    def __truediv__(self, divisor):
        denominator = divisor.Re**2 + divisor.Im**2
        if denominator == 0:
            raise ValueError('Division by zero error.')
        quotient_Re = (self.Re*divisor.Re + self.Im*divisor.Im)/denominator
        quotient_Im = (self.Im*divisor.Re - self.Re*divisor.Im)/denominator
        quotient = Complex(quotient_Re, quotient_Im)
        return quotient

    def conjugate(self):
        result = Complex(self.Re, -self.Im)
        return result

    def modulus(self):
        return (self.Re**2 + self.Im**2)**(1/2)

    def argument(self):
        if self.Re == 0 and self.Im == 0:
            raise ValueError('Incorrect complex form conversion (alg to trig - 0 value)')
        if self.Re < 0 and self.Im == 0:
            return pi
        else:
            return 2*atan(self.Im/(self.modulus()+self.Re))
            
        

