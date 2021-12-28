import unittest
from signals.signal import Signal
from signals.perturbations.perturbation import Perturbation
from signals.perturbations.step_perturbation import StepPerturbation
from signals.perturbations.spike_perturbation import SpikePerturbation

amps = [0,1,2,3,4]
pers = [0,1,2,3,4]
phases = [0,1,2,3,4]
trans = [0,0.1,0.15,0.25]
means = [0,1,2,3,4]
stds = [1,2,3,4,5]

class TestSignal(unittest.TestCase):
    def test_createSignal(self):
        for a,p,ph,t,mu,sigma in zip(amps,pers,phases,trans,means,stds):
            test_signal = Signal(amp=a,per=p,phas=ph,trans=t,mean=mu,std=sigma)
            base_dict = {'_amplitude': a, '_period': p, '_phase': ph, '_translation': t}
            noise_dict = {'_mean':mu,'_deviation':sigma}
            self.assertEqual(test_signal._baseline.__dict__,base_dict)
            self.assertEqual(test_signal._noise.__dict__,noise_dict)
            self.assertEqual(test_signal._perturbations,None)

    def test_addPerturbation(self):
        for a,p,ph,t,mu,sigma in zip(amps,pers,phases,trans,means,stds):
            test_signal = Signal(amp=a,per=p,phas=ph,trans=t,mean=mu,std=sigma)
            test_pert = Perturbation()
            test_signal.add_perturbation(test_pert)
            self.assertEqual(len(test_signal._perturbations),1)
            self.assertRaises(TypeError,test_signal.add_perturbation,{})

    def test_arithmetic_sample(self):
        test_signal = Signal(amp=4,per=1.5,phas=0,trans=2,mean=0.15,std=0.1)
        test_step = StepPerturbation(t0=2,support=3,strength=3,step=3.5,dir=1)
        test_spike = SpikePerturbation(t0=6,support=3,strength=8,position=7.5,width=0.8)
        test_signal.add_perturbation(test_step)
        test_signal.add_perturbation(test_spike)
        type,sample = test_signal.create_arithmetic_sample(t0=0,t1=10)
        self.assertEqual(type,'PERT')
        self.assertEqual(len(sample),100)
        sample.to_csv('test_spike_senal.csv',index=False)


if __name__ == '__main__':
    unittest.main()