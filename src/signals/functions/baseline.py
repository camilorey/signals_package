import math
from .function import Function

class BaseLine(Function):
    """
    The class that will contain the analytical function that _baselines_ a signal. This is a simple
    parametric function of the form
    B(t) = A sin(wt+r)
    this method is expected to contain the following parameters:
        amp: to set the amplitude (default value is 0)
        per: to set the period (default value is 0)
        phas: to set the phase of the signal (default value is 0)
        trans: to set the translation of the signal (default value is 0)
    """

    def construct_function(self,kwargs:dict):
        """
        BaseLine implementation of the construct_function(kwargs) method
        :param kwargs: a dictionary containing perhaps the parameters of a BaseLine Function. The Dictionary needs
        to hold parameters such as amp (for self._amplitude), per (for self._period), phas for (self._phase) or trans
        for (self._translation).
        :return: None. BaseLine attributes are set internally.
        """
        self.set_parameter(kwargs, '_amplitude', 'amp', 0)
        self.set_parameter(kwargs, '_period', 'per', 0)
        self.set_parameter(kwargs, '_phase', 'phas', 0)
        self.set_parameter(kwargs, '_translation', 'trans', 0)

    def calculate(self,t:float)->float:
        """
        The rule that composes the function.
        :param t: (float) the value at which we want to return the function
        :return: the value calculated at t (raises TypeError if t is not int or float).
        """
        if type(t) not in [float,int]:
            raise TypeError("Error function variable is not numeric ")
        else:
            sin_arg = self._period*t + self._phase
            return self._amplitude*math.sin(sin_arg) + self._translation

    def wave_length(self):
        if self._period == 0:
            return math.inf
        else:
            return 2*math.pi/self._period

    def _sin_arg_string(self):
        """
        This method creates the argument of the BaseLine sine function.
        :return: w*t+r or the empty string
        """
        sin_arg = ''
        if self._period != 0:
            if abs(self._period)!= 1:
                sin_arg += "{:,.2f}t".format(self._period)
            else:
                if self._period == 1:
                    sin_arg += "t"
                else:
                    sin_arg += "-t"
        if self._phase !=0:
            if self._phase <0:
                sin_arg += "{:,.2f}".format(self._phase)
            else:
                if sin_arg == '':
                    sin_arg = "{:,.2f}".format(self._phase)
                else:
                    sin_arg += "+{:,.2f}".format(self._phase)
        return sin_arg

    def _create_sine(self):
        """
        Method to print the sine part of the baseline function
        :return: a form A*Sin(w*t+r) or empty string if A=0 or w*t+r==0.
        """
        sin_arg = self._sin_arg_string()
        if self._amplitude == 0 or sin_arg == '':
            return  ''
        else:
            if self._amplitude ==1:
                return "Sin({})".format(sin_arg)
            elif self._amplitude == -1:
                return "-Sin({})".format(sin_arg)
            else:
                return "{:,.2f}Sin({})".format(self._amplitude,sin_arg)

    def __repr__(self):
        repr = 'BaseLine(amp={},per={},phas={},trans={})'.format(self._amplitude,
                                                                 self._period,
                                                                 self._phase,
                                                                 self._translation)
        return repr

    def __str__(self):
        func = "S(t)="
        sin_func = self._create_sine()
        if sin_func != '':
            func = "S(t)={}".format(sin_func)
            if self._translation !=0:
                if self._translation < 0:
                    func += "{:,.2f}".format(self._translation)
                else:
                    func += "+{:,.2f}".format(self._translation)
        else:
            func= "S(t)=0.0"
        return func






