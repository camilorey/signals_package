import warnings
import numpy as np
from .perturbation import Perturbation

class SpikePerturbation(Perturbation):
    """
    This class will simulate a spike perturbation, a single value that is emitted at time _t0,
    that causes a Petrurbation in the form a Dirac Function (with a support of 1.0).

    Parameters to construct a Spike Perturbation are two:
        spike: the amplitude of the spike to construct
        t0: the time at which the spike is to take place
    """
    def construct_function(self,kwargs:dict):
        """
        SpikePerturbation implementation of the construct_function(kwargs) method
        :param kwargs: a dictionary containing perhaps the parameters of a Spike Perturbation Function.
        The Dictionary needs to hold parameters such as spike (for self._amplitude), spike_start (for self._position)
        and support for (_spike_support).
        :return: None. Spike Perturbation attributes are set internally.
        """
        if 'position' in kwargs:
            p = kwargs['position']
            is_in_support = self.check_parameter_in_support(p)
            if is_in_support == False:
                warnings.warn('Warning: Spike width is outside of the support.')
        self.set_parameter(kwargs,'_width','width',0.3)
        self.set_parameter(kwargs,'_position','position',0.8)

    def perturbation_function(self,t:float) ->float:
        """
        This is the function that will calculate the spike of the perturbation. if within the
        spike, it will return a random number close to the strength level, otherwise it will return
        random numbers only 10% of the strength of the perturbation
        :param t: t (float)
        :return: N(_strength,_strength*0.15) if within the spike, 0.1*N(_strength,_strength*0.15) otherwise
        """

        if abs(t-self._position)< self._width/2:
            return np.random.normal(loc=self._strength,scale=self._strength*0.15,size=1)[0]
        else:
            return np.random.normal(loc=self._strength,scale=self._strength*0.15,size=1)[0]*0.1