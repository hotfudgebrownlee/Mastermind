class Player:
    """
    Stereotype: 
        Information Holder
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._move = None

    def get_name(self):
        """
        Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name
    
    def get_move(self):
        """
        Returns the player's last move (an instance of Move). If the player 
        hasn't moved yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._move

    def set_move(self, move):
        """
        Sets the player's last move to the given instance of Move.

        Args:
            self (Player): an instance of Player.
            move (Move): an instance of Move
        """
        self._move = move

    