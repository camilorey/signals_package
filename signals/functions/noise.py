import numpy
import warnings
from .function import Function

class Noise(Function):
    """
    The class that will contain the noise factor that _flavors_ a signal, the noise provided here
    is a simple Gaussian noise (time invariant) of the form
    R(t) ~ N(mu,sigma)
    the constructor of this Class expects parameters like
        mean: to set the mean of the Gaussian Noise (default value is 0)
        std: to set the standard deviation of the gaussian noise (default value is 1)
    """
    def construct_function(self,kwargs:dict):
        """
        Noise implementation of the construct_function(kwargs) method
        :param kwargs: a dictionary containing perhaps the parameters of the Noise. The Dictionary needs
        to hold parameters such as mean (for self._mean) or std (for self._deviation)
        :return: None. Noise attributes are set internally.
        """
        self.set_parameter(kwargs, '_mean', 'mean', 0)
        if 'std' in kwargs:
            std = kwargs['std']
            if std <=0:
                warnings.warn("Warning: Deviation cannot be negative. Setting default value (sigma=1) instead")
            else:
                self.set_parameter(kwargs, '_deviation', 'std', 1)
        else:
            self.set_parameter(kwargs, '_deviation', 'std', 1)

    def __str__(self):
        return 'N({:,.2f},{:,.2f})'.format(self._mean,self._deviation)

    def __repr__(self):
        return 'Noise(mean={},std={})'.format(self._mean,self._deviation)

    def calculate(self,t:float)->float:
        """
        The rule that produces the random noise.
        :param t: (float) the value at which we want to return the function
        :return: random number for value t (raises TypeError if t is not int or float).
        """
        if type(t) not in [float,int]:
            raise TypeError("Error function variable is not numeric ")
        else:
            noise_number = numpy.random.normal(loc=self._mean,
                                               scale=self._deviation,
                                               size=1)[0]
            return noise_number