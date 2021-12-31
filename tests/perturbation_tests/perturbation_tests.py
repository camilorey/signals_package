import numpy as np
import unittest
from src.signals import Perturbation
from src.signals import SpikePerturbation
from src.signals import StepPerturbation

class PerturbationTest(unittest.TestCase):

    def test_createPerturbation(self):
        test_pert = Perturbation()
        self.assertEqual(test_pert.__dict__,{'_t0':0.5,'_support':0.25,'_strength':1})

    def test_perturbationValues(self):
        t_values = list(np.linspace(start=0,stop=1.0,num=50,endpoint=True))
        test_pert = Perturbation()
        for t in t_values:
            t_float = float(t)
            P_t = test_pert.calculate(t_float)
            if t_float >=0.5 and t_float <0.75:
                self.assertEqual(P_t,1)
            else:
                self.assertEqual(P_t,0)

    def test_createSpike(self):
        test_spike = SpikePerturbation(t0=0.8,strength=8,support=10,position=1.2,width=0.3)
        self.assertEqual(test_spike.__dict__,{'_t0':0.8,'_support':10,'_strength':8,'_position':1.2,'_width':0.3})

    def test_spikeValues(self):
        s,p,w = 2,1.2,0.3
        supp,t0 = 2,0.8
        test_spike = SpikePerturbation(t0=0.8,support=supp,strength=s,position=p,width=w)
        t_values = list(np.linspace(start=0, stop=4.0, num=50, endpoint=True))
        epsilon = 0.09
        for t in t_values:
            t_float = float(t)
            P_t = test_spike.calculate(t_float)
            if t_float < t0 or t_float> t0+supp:
                #case outside the support
                self.assertEqual(P_t,0)
            else:
                if abs(t-p) < w/2:
                    self.assertTrue(s*(1-0.4) <= P_t <= s*(1+0.4))
                else:
                    self.assertTrue(0.1*s*(1-0.4) <= P_t <= 0.1*s*(1+0.4))

    def test_stepConstruction(self):
        s = 2
        supp, t0,step,dir = 2, 0.8, 1.2,-1
        test_step = StepPerturbation(t0=t0,support=supp,strength=s,step=step,dir=dir)
        t_values = list(np.linspace(start=0, stop=4.0, num=50, endpoint=True))
        epsilon = 0.09
        for t in t_values:
            t_float = float(t)
            P_t = test_step.calculate(t_float)
            if t_float < t0 or t_float> t0+supp:
                self.assertEqual(P_t,0)
            else:
                if dir > 0:
                    if t < step:
                        self.assertTrue(-s*(1+0.3) <= P_t <= -s*(1-0.3))
                    else:
                        self.assertTrue(s*(1-0.3) <= P_t <= s*(1+0.3))
                else:
                    if t > step:
                        self.assertTrue(-s*(1+0.3) <= P_t <= -s*(1-0.3))
                    else:
                        self.assertTrue(s*(1-0.3) <= P_t <= s*(1+0.3))








if __name__ == '__main__':
    unittest.main()