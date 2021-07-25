import unittest
from complex_num import Complex

class TestComplex(unittest.TestCase):
    
    def setUp(self):
        self.Z1 = Complex(0,0)
        self.Z2 = Complex(11,-22)
        self.Z3 = Complex(-12,43)
        self.Z4 = Complex(99,11)
        self.Z5 = Complex(-64,-36)
        self.Z6 = Complex(-11,0)

    def test_Print(self):
       self.assertEqual('(0+0i)', self.Z1.__str__())
       self.assertEqual('(11-22i)', self.Z2.__str__())
       self.assertEqual('(-12+43i)', self.Z3.__str__())
       self.assertEqual('(99+11i)', self.Z4.__str__())
       self.assertEqual('(-64-36i)', self.Z5.__str__())

    def test_Addition(self):
        self.assertEqual(Complex(99,11) , self.Z1 + self.Z4)
        self.assertEqual(Complex(-76,7) , self.Z3 + self.Z5) 
        self.assertEqual(Complex(-1,21) , self.Z2 + self.Z3) 
        self.assertEqual(Complex(-1,21) , self.Z3 + self.Z2) 
        self.assertEqual(Complex(-128,-72) , self.Z5 + self.Z5)
    
    def test_Substraction(self):
        self.assertEqual(Complex(-99,-11) , self.Z1 - self.Z4)
        self.assertEqual(Complex(52,79) , self.Z3 - self.Z5) 
        self.assertEqual(Complex(23,-65) , self.Z2 - self.Z3) 
        self.assertEqual(Complex(-23,65) , self.Z3 - self.Z2) 
        self.assertEqual(Complex(0,0) , self.Z5 - self.Z5) 
    
    def test_Multiplication(self):
        self.assertEqual(Complex(0,0) , self.Z1 * self.Z4)
        self.assertEqual(Complex(2316,-2320) , self.Z3 * self.Z5) 
        self.assertEqual(Complex(814,737) , self.Z2 * self.Z3) 
        self.assertEqual(Complex(814,737) , self.Z3 * self.Z2) 
        self.assertEqual(Complex(2800,4608) , self.Z5 * self.Z5) 
    
    def test_Division(self):
        with self.assertRaises(ValueError):
            self.Z5 / self.Z1
        self.assertEqual(Complex(0,0) , self.Z1 / self.Z4)
        self.assertEqual(Complex(1,0) , self.Z5 / self.Z5)
        Z0 = self.Z3 / self.Z4
        self.assertAlmostEqual(Z0.Re, -0.07206, 5)
        self.assertAlmostEqual(Z0.Im, 0.44235, 5)

    def test_Conjugate(self):
        self.assertEqual(Complex(0,0), self.Z1.conjugate())
        self.assertEqual(Complex(-12,-43), self.Z3.conjugate())
        self.assertEqual(Complex(-64,36), self.Z5.conjugate())
        
    def test_Modulus(self):
        self.assertEqual(self.Z1.modulus(), 0)
        self.assertAlmostEqual(self.Z3.modulus(), 44.64303, 5)

    def test_argument(self):
        with self.assertRaises(ValueError):
            self.Z1.argument()
        self.assertAlmostEqual(self.Z6.argument(), 3.14159, 5)
        self.assertAlmostEqual(self.Z4.argument(), 0.110657, 5)
        self.assertAlmostEqual(self.Z5.argument(), -2.62920, 5)

if __name__ == "__main__":
    unittest.main()