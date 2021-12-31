import unittest
from src.signals import Function

class TestFunction(unittest.TestCase):

    def test_functionCreate(self):
        test_func = Function(param1=5,param2=3)
        self.assertEqual(test_func.__dict__,{'param1':5,'param2':3})

    def test_functionCreateNonNumeric(self):
        self.assertRaises(TypeError,Function.__init__,param1=5,param2='string')

    def test_functionCreateRaisesError(self):
        self.assertRaises(TypeError,Function.__init__,param='string')

    def test_evaluate(self):
        test_func = Function()
        self.assertEqual(test_func.calculate(0),0)

    def test_calculate(self):
        test_func = Function()
        self.assertRaises(TypeError,test_func.evaluate,'w')

if __name__ == '__main__':
    unittest.main()
