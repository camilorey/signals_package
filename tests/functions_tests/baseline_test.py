import unittest
import math
from src.signals import BaseLine

class BaselineTest(unittest.TestCase):

    def test_functionDefaultCreate(self):
        base_test = BaseLine()
        base_dict = {'_amplitude':0,'_period':0,'_phase':0,'_translation':0}
        self.assertEqual(base_test.__dict__,base_dict)

    def test_functionParamCreate(self):
        base_test = BaseLine(amp=1,per=1,phas=1,trans=1)
        base_dict = {'_amplitude': 1, '_period': 1, '_phase': 1, '_translation': 1}
        self.assertEqual(base_test.__dict__, base_dict)

    def test_print(self):
        self.assertEqual(BaseLine().__str__(), 'S(t)=0.0')
        self.assertEqual(BaseLine(amp=1, per=1, phas=0, trans=0).__str__(), 'S(t)=Sin(t)')
        self.assertEqual(BaseLine(amp=1, per=1, phas=0, trans=1).__str__(), 'S(t)=Sin(t)+1.00')
        self.assertEqual(BaseLine(amp=1,per=1,phas=1,trans=2).__str__(),'S(t)=Sin(t+1.00)+2.00')

    def test_repr(self):
        test_func= BaseLine(amp=1, per=1, phas=0, trans=0)
        self.assertEqual(test_func.__repr__(),'BaseLine(amp=1,per=1,phas=0,trans=0)')

    def test_funcEvaluate(self):
        test_func =BaseLine(amp=1,per=1,phas=0,trans=0)
        self.assertRaises(TypeError,test_func.evaluate,'string')

    def test_funcValues(self):
        amps = [1,2,3]
        periodos = [1,2,3]
        fases = [1,2,3]
        traslaciones = [1,2,3]
        t_vals = [0,1,math.pi/4,math.pi/3,math.pi]
        for a,p,f,tr in zip(amps,periodos,fases,traslaciones):
            test_func = BaseLine(amp=a,per=p,phas=f,trans=tr)
            for t in t_vals:
                S_t = a*math.sin(p*t+f)+tr
                self.assertEqual(test_func.calculate(t),S_t)

if __name__ == '__main__':
    unittest.main()