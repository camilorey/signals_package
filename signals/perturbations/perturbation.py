import numpy as np
from signals.functions.function import Function

class Perturbation(Function):
    """
    This is the base Class for all perturbations. A perturbation is distinguished for having some basic parameters
    that allow us to apply the perturbation within a time period (periodically)
    t0: the time at which the perturbation is supposed to start
    support: the width of the perturbation (i.e. time-span)
    amplitude: the amplitude of the perturbation

    """
    def __init__(self,**kwargs):
        args_wrong = self.check_numeric(kwargs)
        if args_wrong is not None:
            raise TypeError("The Following parameters are not numeric: {}".format(args_wrong))
        else:
            self.set_base_parameters(kwargs)
            self.construct_function(kwargs)

    def set_base_parameters(self,kwargs:dict):
        """
        BaseLine implementation of the construct_function(kwargs) method
        :param kwargs: a dictionary containing perhaps the parameters of a BaseLine Function. The Dictionary needs
        to hold parameters such as amp (for self._amplitude), per (for self._period), phas for (self._phase) or trans
        for (self._translation).
        :return: None. BaseLine attributes are set internally.
        """
        self.set_parameter(kwargs, '_t0', 't0', 0.5,check_sign=True)
        self.set_parameter(kwargs, '_support', 'support', 0.25,check_sign=True)
        self.set_parameter(kwargs, '_strength', 'strength', 1,check_sign=True)

    def check_parameter_in_support(self,param:float)->bool:
        """
        This method is to check that a perturbation parameter is within the support of the function.
        This will be useful in the case of spike and step functions where the changes in the function
        must occur within the support of the function.
        :param param: the param we wish to check within the support
        :return: True if the parameter is within the support, False otherwise.
        """
        if type(param) not in [int,float]:
            raise TypeError("Type Error: parameter {} is not numeric".format(param))

        return self._t0 <= param and param <= self._t0 + self._support

    def perturbation_function(self,t:float)->float:
        """
        This is the function that will contain the perturbation logic and will be implemented
        differently by every class.
        :param t: a number
        :return: float
        """
        return self._strength

    def _char_of_support(self,t:float)->float:
        """
        This function determines wether we are within the support of the function or not
        :param t: t (numeric value) to see if within the support
        :return: 1 if within the support 0 otherwise
        """
        if t > self._t0 and t < self._t0 + self._support:
            return 1
        else:
            return 0

    def calculate(self,t:float)->float:
        """
        This is the calculate function from the Function class. What distinguishes
        perturbations is that before the _t0 parameter, there will be no perturbation.
        :param t: the argument of the function (numeric type). It raises error if t is not numeric.
        :return: 0 before _t0 argument and perturbation_function(t) otherwise.
        """
        if type(t) not in [float,int,np.float64]:
            raise TypeError("Error: function variable is not numeric ")
        else:
            return self.perturbation_function(t)*self._char_of_support(t)