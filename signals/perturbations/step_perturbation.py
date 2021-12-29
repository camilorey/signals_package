import warnings
import numpy as np
from .perturbation import Perturbation

class StepPerturbation(Perturbation):
    """
    This class will simulate a Step perturbation, with a support beginning at _t0 and ending in _t0+_support,
    that causes a Petrurbation in the form a Step Function.

    Parameters to construct a Step Perturbation are two:
        strength: the amplitude of the step to take
        step: the time at which the step is to take place
        direction: the direction in which the step is to happen (before (-1) or after t0 (+1)).
    """
    def construct_function(self,kwargs:dict):
        """
        StepPerturbation implementation of the construct_function(kwargs) method
        :param kwargs: a dictionary containing perhaps the parameters of a Step Perturbation Function.
        The Dictionary needs to hold parameters such as spike (for self._amplitude) or t0 (for self._t0)
        to create a step.
        :return: None. Step Perturbation attributes are set internally.
        """
        if 'step' in kwargs:
            w = kwargs['step']
            is_in_support = self.check_parameter_in_support(w)
            if not is_in_support:
                warnings.warn('Warning: Step position is outside of support.')
        self.set_parameter(kwargs,'_step','step',1)
        self.set_parameter(kwargs,'_direction','dir',1)

    def perturbation_function(self, t: float) -> float:
        """
        For the Step function, we will return a random number N(strength,strength*0.15) but the
        sign of the number will be positive if t>step and negtive if t<step. If the direction is reversed
        then the signs will interchange.
        :param t: a number
        :return: float
        """
        random_number = np.random.normal(loc=self._strength,
                                         scale=self._strength * 0.05,
                                         size=1)[0]
        if t < self._step:
            random_number *=-1
        else:
            random_number *= 1
        return random_number*self._direction