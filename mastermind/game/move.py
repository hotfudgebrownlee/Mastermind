class Move:
    """
    Stereotype: 
        Information Holder
    """
    def __init__(self, guess):
        """The class constructor.
        Args:
            self (Move): an instance of Move.
        """
        self._guess = guess 
    def get_guess(self):
        """Returns the move that is either correct or not.
        Args:
            self(Move): an instance of move.
        """  
        return self._guess