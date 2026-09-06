class C:
    ''' A class ''' 
    def __init__(self, id=0):
        """
        >>> from tinylm.scratch import C
        >>> C() # doctest: +ELLIPSIS
        <...C object at 0x...>
        """        
        self.id = id
