#test_simple_calculator
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        #set up the simple calculatore instance before each instance.
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(0.34, 0.12), 0.46)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(1.45, 0.55), 0.9)
        

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -2), 2)
        self.assertEqual(self.calc.multiply(0, 3), 0)
        self.assertEqual(self.calc.multiply(1.5, 4), 6)
        self.assertEqual(self.calc.multiply(0, 0), 0)


    def test_division(self):
        self.assertEqual(self.calc.divide(3, 3), 1)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        self.assertEqual(self.calc.divide(6, 1.5), 4)
        self.assertEqual(self.calc.divide(-1, 4), -0.25)
        self.assertEqual(self.calc.divide(1.5, 0.5), 3)

        #Test division by Zero should return "None"
        self.assertIsNone(self.calc.divide(1, 0))
        self.assertEqual(self.calc.divide(-1, 0))

# Additional tests for edge cases
    def test_edge_cases(self):
        #Test additional edge cases.
        # Test adding, subtracting, and multiplying large numbers
        self.assertEqual(self.calc.add(10*6, 106), 2 * 10*6)
        self.assertEqual(self.calc.subtract(10*6, 105), 9 * 10*5)
        self.assertEqual(self.calc.multiply(10*6, 106), 10*12)

        # Test dividing by a very small number
        self.assertAlmostEqual(self.calc.divide(1, 1e-6), 1e6)
        self.assertAlmostEqual(self.calc.divide(-1,1e-6),-1e6)

if __name__ == "_main_":
   unittest.main()