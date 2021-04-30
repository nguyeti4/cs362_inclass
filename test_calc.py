import unittest
import calc

class testCase(unittest.TestCase):
    def test_add(self):
        result = calc.add(12,2)
        self.assertEqual(result,4)
    def test_add2(self):
        result = calc.add(12,2)
        self.assertEqual(result,10)
    def test_sub(self):
        result = calc.sub(12,2)
        self.assertEqual(result,10)
    def test_mul(self):
        result = calc.mul(12,2)
        self.assertEqual(result,24)
    def test_mul2(self):
        result = calc.mul(12,2)
        self.assertEqual(result,20)
    def test_div(self):
        result = calc.div(12,3)
        self.assertEqual(result,4)
    def test_div2(self):
        result = calc.div(12,0)
        self.assertEqual(result,0)
    
        
