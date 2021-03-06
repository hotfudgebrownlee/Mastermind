from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _board (Board): An instance of the class of objects known as Board.
        _console (Console): An instance of the class of objects known as Console.
        _keep_playing (boolean): Whether or not the game can continue.
        _move (Move): An instance of the class of objects known as Move.
        _roster (Roster): An instance of the class of objects known as Roster.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()
        self.num_players = 0

    def start_game(self):
        """Starts the game loop to control sequence of play.

        Args:
            self(Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares game. That means getting player names and adding them
        to the roster.

        Args:
            self (Director): An instance of Director.
        """
        prompt = "How many players? (2-6): "
        self.num_players = self._console.read_number(prompt)
        while True:
            if(self.num_players > 6):
                self._console.write("Please choose less than 7 players.")
                self.num_players = self._console.read_number(prompt)
            elif(self.num_players < 2):
                self._console.write("Please choose more than 1 player.")
                self.num_players = self._console.read_number(prompt)
            else:
                break
        for i in range(self.num_players):
            p_name = self._console.read(f'Player {(i+1)}, please enter your name: ')
            p_code = self._board.get_code()
            player = Player(p_name,p_code)
            self._roster.add_player(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. For this
        game, gets move from current player.

        Args:
            self(Director): An instance of Director.
        """
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn")
        prompt = "Please enter your guess (1000-9999): "
        guess = self._console.read_number(prompt)
        while True:
            if(guess < 1000):
                self._console.write("Please enter a guess over 1000.")
                guess = self._console.read_number(prompt)
            elif(guess > 9999):
                self._console.write("Please enter a guess under 9999.")
                guess = self._console.read_number(prompt)
            else:
                break
        move = Move(guess)
        player.set_move(move.get_guess())

    def _do_updates(self):
        """Updates important game information for each round of play. For
        this game, the board is updated with the current guess.

        Args:
            self(Director): An instance of Director.
        """
        player = self._roster.get_current()
        move = player.get_move()
        code = player.get_code()
        self._board.apply(move, code)
        player.set_hint(self._board.get_hint())

    def _do_outputs(self):
        """Outputs the important game information for each round of play.
        For this game, a hint is printed from the board. If the code
        matches the guess exactly, a winner is declared.

        Args:
            self(Director): An instance of Director.
        """
        if self._board.matches_code():
            winner = self._roster.get_current()
            name = winner.get_name()
            self._console.write(f'\n{name} won!')
            self._keep_playing = False
        print()
        for _ in range(self.num_players):
            self._roster.next_player()
            move = self._roster.get_current().get_move()
            hint = self._roster.get_current().get_hint()
            name = self._roster.get_current().get_name()
            text = (f"Player {name}: {move}, {hint}")
            self._console.write(text)
        self._roster.next_player()