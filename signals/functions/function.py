import warnings
class Function:
    """"This class is the abstract base for function calculation"""

    def __init__(self,**kwargs):
        args_wrong = self.check_numeric(kwargs)
        if args_wrong is not None:
            raise TypeError("The Following parameters are not numeric: {}".format(args_wrong))
        else:
            self.construct_function(kwargs)

    def construct_function(self,kwargs):
        """
        This method will assign the attributes to the function.
        :param kwargs: A dictionary containing the parameters that the function will use
        :return: None
        """
        for attr_name in kwargs:
            self.set_parameter(kwargs,attr_name,attr_name,0)

    def set_parameter(self,param_dict,nom_attr,nom_param,default_value):
        """
        This method asserts and assigns the attributes of a baseline signal
        :param param_dict:
        :param nom_attr:
        :param nom_param:
        :param default_value:
        :return:
        """
        if nom_param not in param_dict:
            warn = 'Warning: parameter {} not in kwargs, using {} instead'.format(nom_param,default_value)
            warnings.warn(warn)
            self.__setattr__(nom_attr,default_value)
        else:
            value = param_dict[nom_param]
            if type(value) not in [int,float]:
                error = 'Type Error: Parameter {} not of numeric type, using {} instead'.format(nom_param,default_value)
                raise TypeError(error)
                self.__setattr__(nom_attr,default_value)
            else:
                self.__setattr__(nom_attr,value)

    def check_numeric(self,kwargs)->list:
        """
        Checks if a list of parameters is only composed of numbers
        :param kwargs: the dictionary of parameters that we want to check
        :return: list of parameters that are not numbers
        """
        arg_wrong = []
        for param_name in kwargs:
            val = kwargs[param_name]
            if type(val) not in [float,int]:
                arg_wrong.append(param_name)
        if len(arg_wrong) == 0:
            return None
        else:
            return arg_wrong

    def evaluate(self,t:float)->tuple:
        """
        Method to calculate a single point of the function given a value of t
        :param t: the value at which we want to calculate the function
        :return: tuple, (t,f(t)) of the function calculated at a value
        """
        if type(t) not in [float,int]:
            raise TypeError(f'Argument t is not a number')
            return None
        else:
            return (t,self.calculate(t))

    def calculate(self,t:float)->float:
        """
        The rule that composes the function.
        :param t: (float) the value at which we want to return the function
        :return: the value calculated at t.
        """
        return 0
