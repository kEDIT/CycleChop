# This submodule contains definitions for the Signal class 
# and some useful methods for common processing needs.
# (TODO: smoothing, autocorrelation).
#
# Methods on the signal class are just some syntactic sugar wrapping 
# numpy and pandas methods for easier use in larger application context.

class Signal:
    """
    Signal class represents a 1-D vector of values with optional 1-D paramaterization 
    (from a time vector, for example). Parameter vectors in the following documentation 
    are referred to as time, but in principal they can be anything (e.g. Voltage 
    measured from a sensor, some accumulator value, etc.)

    Note: 
        Although instances of the signal class represent 1-dimensional data, if they are  
        parameterized by a time variable and the corresponding time values are needed for 
        some calculation, the signal must be supplied as a 2-D collection of vectorized
        data, with one vector corresponding to time. There is no need to set `param=True`
        if the input is 2-D, however the signals should have appropriately labeled columns or rows.

        Alternatively, if the input supplied is 1-D, but the `param` argument is set to `True`,
        a second index will be attached containing a boolean mask in place of time values, allowing for
        time-dependent calculations to be performed later if a vector of time values is passed 
        to the method (vector must be the same shape as the boolean mask, ie same shape as the raw signal data).
    
    Attributes:
        _siglist: names of signals extracted from column labels of raw signal data
        _name: name of signal (default: first column name not equal to or containing `time`, if `param` is 
            set to True and signal input is g.e. to 2-D. Otherwise, it is the index label or first entry
            of the data's primary axis).
        _unit: unit value of signal (eg "mm", "N","Pa",etc) (default: None).
        _cleaned: boolean value indicating whether the signal data has been cleaned (default: True). If the value
            is set to False, user defined preconditioning routines can be supplied via the Polisher class. 
            TODO: Add Polisher class definition from notes.
        _data: underlying data
    """
    def __init__(self,sig=None,name=None,param=True,cleaned=True):
        if sig is not None and param=None:
            try:
                self._siglist = sig.columns.tolist()
                dims = sig.shape
                if len(dims) > 2:
                    raise #TODO: define exception raised here, make sure it's caught in following except block!
                elif len(dims) == 2 and (len(dims[0]) != len(dims[1])):
                    raise #TODO: define exception raised here, make sure it's caught in following except block!
                else:
                    #len(dim) is at least 1-D
                    self._samplesize = len(dim)
            except: #Defined exceptions
                #If possible, logic for handling exceptions w/o having to propagate them farther should go here.
                raise #TODO: define error type from Pandas or builtin error type
            if name is not None: 
                try:
                    self._data = sig.loc[:,name]
                    self._name = name
                except KeyError as e:
                    #TODO: revert to default routine for identifying signal name and values
                
                #TODO: furnish test_vector; don't leave as simple example, move following piece of code into seperate function
                test_vector = ["Time","(s)","min"] #TODO: 
                poss_time = [[substr.lower() in i.lower() for substr in test_vector] for i in self._siglist] 
                poss_time = list(map(lambda x: any(x[:]),poss_time)) #more robust recognition? 

                #finish out setting self._data and other params here

