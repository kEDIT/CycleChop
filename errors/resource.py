# Defines Exceptions for invalid resource handle invocations and IO operations in CycleChop.
# Also includes some basic wrapper functions for log formatting and debugging.

class BaseError(Exception):
    """Error Base Class Resource Handling & IO Operations in CycleChop Package."""
    
    def __init__(self, msg=None):
        if msg is None:
            msg = "\nERROR\n"
        super(BaseError,self).__init__(msg)

#TODO: Write implementation for ResourceError
def LogWrap(error, head=None,tail=None):
    """
    Function returns an instance of the nested `WrappedError` class, which extends the inherited Error class behavior
    by wrapping the output of Error.format() with heading and/or 
    trailing formatted text bodies, for logging/debugging purposes.
    """    
    class WrappedError(error):
        def __init__(self):
            error.__init__(self)
            self.set_error_head(head)
            self.set_error_tail(tail)

        def set_error_head(self,head):
            if head is not None:
                self._head = head

        def set_error_tail(self,tail):
            if tail is not None:
                self._tail = tail

class StubBase:
    """ 
    A string utility class auto-formatting error strings generated by various exceptions.
    
    Attributes:
        _delim: Delimiter added to both sides of basestr (default=None).
        _lhsd: Left-hand-side-delimiter. Used if split parameter of constructor is set to True (default=None).
        _rhsd: Right-hand-side-delimeter. Used if split parameter of constructor is set to True (default=None).
        _split: Boolean value used for changing delimiter state from single to split (default=False).
    """    
    def __init__(self,delim=None,lhsd=None,rhsd=None,split=False):
        self._basestr = " {} "
        self.split = split
        if self.split:
            self._lhsd = lhsd
            self._rhsd = rhsd
        else:
            self._delim = delim
    
    def format(self,string=None):
        if string is None:
            basestr = ""
            return basestr
        else:
            basestr = self._basestr.format(string)
        
        if self.split:
            if self._lhsd is not None and self._rhsd is not None:
                basestr = "{0} {1} {2}".format(self._lhsd,basestr,self._rhsd)
            elif self._lhsd is not None:
                basestr = "{0} {1}".format(self._lhsd,basestr)
            elif self._rhsd is not None:
                basestr = "{0} {1}".format(basestr,self._rhsd)
            else:
                #Raise a stub generation error or something like that.
                pass
        else:
            if self._delim is not None:
                basestr = "{0} {1} {0}".format(self._delim,basestr)
            else:
                #Defaults for 'split' param and delim are False & None, respectively. No exception can be raised here.
                pass

        return basestr

class ResourceError(BaseError):
    """
    Exception raised when resource handle DNE or could not be found/retrieved
    
    Attributes:
        -- Note: Default values from baseclass are used if attributes aren't defined.
        Message: Error message string printed when a resource error occurs.
        Expression: Expression which failed to evaluate and resulted in the resource error.
        Delim: Delimeter used by error formatter.
    """
    def __init__(self):
        self._message = "RESOURCE ERROR: Failed to identify resource handle"
        self._expression = "No Expression Available"
        self._delim = "\n------------------\n" 
    #Define _message property
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self,value):
        self._message = value
    
    @message.deleter
    def message(self):
        del(self._message)

    #Define _expression property
    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self,value):
        self._expression = value

    @expression.deleter
    def expression(self):
        del(self._expression)

    #Define _delim property
    @property
    def delim(self):
        return self._delim
    
    @delim.setter
    def delim(self,value):
        self._delim = value
    
    @delim.deleter
    def delim(self):
        self._delim=None

    @classmethod
    def format(self):
        msgstub = StubBase(lhsd=getattr(self,'delim'),rhsd='\n',split=True).format(string=getattr(self,'message'))
        expstub = StubBase(rhsd=getattr(self,'delim'),rhsd='\n',split=True).format(string=getattr(self,'expression'))
        super(ResourceError,self).__init__("{0}{1}".format(msgstub,expstub))

