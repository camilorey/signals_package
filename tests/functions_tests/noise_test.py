import unittest
from src.signals import Noise

class NoiseTest(unittest.TestCase):
    def test_str_rep(self):
        mus = [0,1,2,3,4]
        sigmas = [1,2,3,4]
        for m,s  in zip(mus,sigmas):
            noise_test = Noise(mean=m,std=s)
            str_rep = 'N({:,.2f},{:,.2f})'.format(m,s)
            self.assertEqual(noise_test.__str__(),str_rep)

    def test_repr(self):
        mus = [0, 1, 2, 3, 4]
        sigmas = [1, 2, 3, 4]
        for m, s in zip(mus, sigmas):
            noise_test = Noise(mean=m, std=s)
            str_rep = 'Noise(mean={},std={})'.format(m, s)
            self.assertEqual(noise_test.__repr__(), str_rep)

    def test_constructor(self):
        noise_test = Noise(mean=0,std=-1)


if __name__ == '__main__':
    unittest.main()