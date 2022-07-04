from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.parachute import Parachute


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _puzzle (Puzzle): is an instance of Puzzle class
        _is_playing (boolean): Whether or not to keep playing.
        _parachute (Parachute): an instance parachute class
        terminal_service: For getting and displaying information on the terminal.
     
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._parachute = Parachute()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Getting the letter from terminal. Show the hidden word (_ _ _ _) and the parachute

        Args:
            self (Director): An instance of Director.
        """

        #Printing the Hidden word (- - - -)
        self._terminal_service.write_text(self._puzzle.getHiddenWord())

        #Printing the parachute
        self._terminal_service.printList(self._parachute.getParachute())
       
        
        input_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self._puzzle.setLetter(input_letter)
        
    def _do_updates(self):
        """Keeps watch on the parachute is cutting after wrong guess

        Args:
            self (Director): An instance of Director.
        """

        #self._terminal_service.write_text(self._parachute.getWord())

        cut = self._puzzle.updateHiddenWord(self._parachute.getWord())
        if cut == 0:
            self._parachute.cutParachute()
        
    def _do_outputs(self):
        """check if the word was guess correctly or if the user reached the maximun tries to
        stop or continue the game.

        Args:
            self (Director): An instance of Director.
        """
        hidden_Word = self._puzzle.getHiddenWord().replace(" ","")
        word = "".join(self._parachute.getWord())
        
        if self._parachute.getTries() == 0:
            self._terminal_service.printList(self._parachute.getParachute())
            self._is_playing = False

        elif hidden_Word.strip() == word.strip():
            self._is_playing = False

        else:
            self._is_playing= True
