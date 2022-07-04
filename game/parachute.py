import random
from game.word import wordList


class Parachute:
    """The responsability of Parachute class is to generate the word that the user
       need to guess. Also, this class shows parachute and cut it when user guess a 
       letter wrongly.

       Attributes:
        _word_list (array): a list of words from word.py
        _word (String): a word chose randomly from the _word_list array
        _tries (int): the number of tries the user has to guess the word
        _parachute (array): array of strings to draw the parachute
        _end_game (array): array of string to draw a person without parachute to show the 
        use used all his/her tries.

    """
    def __init__(self):
        self._word_list = wordList
        self._word = self._word_list[random.randint(0,(len(self._word_list)-1))] 
        self._tries = 4
        self._parachute = ["  ___",
                           " /___\\",
                           " \   /",
                           "  \ /",
                           "   O",
                           "  /|\\",
                           "  / \\",
                           "      ",
                           " ^^^^^^"]
        self._end_game =  ["   x",
                           "  /|\\",
                           "  / \\",
                           " ^^^^^^"]
    def cutParachute(self):
        self._tries = self._tries - 1
        self._parachute.pop(0)

    def getParachute(self):
        if self._tries > 0:
            return self._parachute
        else:
            return self._end_game
    def getTries(self):
        return self._tries

    def getEndGame(self):
        return self._end_game
    def getWord(self):
        return list(self._word)