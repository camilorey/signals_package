import time
import datetime
import pandas as pd
from src.signals.functions.function import Function
from src.signals.functions.baseline import BaseLine
from src.signals.functions.noise import Noise
from src.signals.perturbations.perturbation import Perturbation


class Signal:
    """
    The Signal class encapsulates a baseline signal alongside with a noise factor
    the properties to create the signal (parameters of the constructor) derive from
    classes like BaseLine and Noise.

    This Signal can be sampled in two ways: specifying the range on which we want to
    sample the signal (i.e. over an interval [t0,t1]) or using the current time as a
    sampling strategy (i.e. from the time the method is called, 200 points with a wait time)
    """

    _DEFAULT_SAMPLE_SIZE = 100
    """
    This MAX_SAMPLING value is the number of default sample size the program will use. 
    """
    def __init__(self,**kwargs):
        """
        Constructor for the signal. Here we only specify the baseline and the noise factors
        read the documentation on the BaseLine and Noise constructors to see what we
        can introduce as kwargs.
        :param kwargs: the dictionary with the parameters to create the baseline and the
        noise factors of the signal.
        """
        self._baseline = BaseLine(**kwargs)
        self._noise = Noise(**kwargs)
        self._perturbations = None
        if 'sample_size' in kwargs:
            val = kwargs['sample_size']
            if type(val) not in [int,float]:
                raise TypeError("Type Error: Sample size is not of numeric.")
            else:
                self._sample_size = round(val)
        else:
            self._sample_size = self._DEFAULT_SAMPLE_SIZE

    def add_perturbation(self,pert):
        """
        Method to add a perturbation to a function. The perturbations should be of
        Function type (otherwise it will raise a TypeError).
        :param pert: The Function that is going to be added as a perturbation of the signal
        :return: None. Perturbation is added to the Signal.
        """
        if not isinstance(pert,Perturbation) and not isinstance(pert,Function):
            raise TypeError("Perturbation is not an instance of Perturbation")
        else:
            if self._perturbations is None:
                self._perturbations = [pert]
            else:
                self._perturbations.append(pert)

    def calculate(self,t):
        """
        MEthod to evaluate the signal at a particular t (of type int or float). If another
        value is provided, the method will raise a TypeError Exception.
        :param t: the time on which we want to caclulate the signal.
        :return: the calculated value of the signal (with and without perturbations).
        """
        value = 0
        try:
            value += self._baseline.calculate(t)
            value += self._noise.calculate(t)
            if self._perturbations is not None:
                for per in self._perturbations:
                    value += per.calculate(t)
        except (Exception,ValueError) as error:
            print("Error ocurred:",error)
            value = None
        finally:
            return value

    def create_arithmetic_sample(self,t0:float=0,t1:float=1):
        """
        This method allows us to sample the signal as if we had a mathematical function, provided with
        the limits of an interval (clopen). If limits are not of numeric type it will raise TypeError,
        as well as if t0 >= t1. It always produces 200 points.

        :param t0: the lower limit of the sample we wish to calculate
        :param t1: the upper limit of the sample we wish to calculate
        :return: a pair (indicator,DF): composed of an indicator (PERT if there are perturbations involved,
        NORMAL if not) and DF a Pandas DataFrame containing the 200 points of the signal sample.
        """
        if t1 == t0:
            raise ValueError("Error: sample size is 0, t0 = t1")
        if t1 < t0:
            raise ValueError("Sampling error: t1 should be larger than t0")
        step = (t1-t0)/float(self._sample_size)
        t = t0
        signal_sample = pd.DataFrame(columns=['t','signal'])
        for i in range(self._sample_size):
            try:
                S_t = self.calculate(t)
                signal_sample = signal_sample.append({'t':t,'signal':S_t},
                                                     ignore_index=True)
                t += step
            except (ValueError,TypeError,Exception) as error:
                print("Could not sample",error)

        type = 'NORMAL'
        if self._perturbations is not None:
            type = 'PERT'

        return type,signal_sample

    def create_time_sample(self,wait_time):
        """
        Creates a MAX_SAMPLE point sample of the signal, aligned by time, starting on the
        time in which the method is called (datetime.now()), and spaces samples according to the
        wait_time parameter. It raises TypeError if wait_time is not numeric, and raises
        ValueError if the wait_time is negative.
        :param wait_time: waiting time between samples (in seconds).
        :return: a pair (indicator,DF): composed of an indicator (PERT if there are perturbations involved,
        NORMAL if not) and DF a Pandas DataFrame containing the 200 points of the signal sample.
        """
        if type(wait_time) not in [int,float]:
            raise TypeError("Error: wait_time is not numeric")
        elif wait_time < 0:
            raise ValueError("Error: wait_time is negative")
        else:
            signal_sample = pd.DataFrame(columns=['t', 'signal'])
            start_time = datetime.now()
            i = 0
            while i < self._sample_size:
                time.wait(wait_time)
                now_time = datetime.now()
                t = (now_time-start_time).timedelta()
                try:
                    S_t = self.evaluate(t)
                    signal_sample = signal_sample.append({'t': now_time, 'signal': S_t},
                                                         ignore_index=True)
                except (ValueError,TypeError,Exception) as error:
                    print("Could not sample signal",error)
                finally:
                    i +=1
        type = 'NORMAL'
        if self._perturbations is not None:
            type = 'PERT'

        return type, signal_sample

