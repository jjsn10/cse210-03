class Puzzle:
    """The responsibility of Puzzle is to generate hiddenWord (_ _ _ _ _) and
       replace the word guest by the use into the hidden word (C _ _ _ _)

       Attributes:
       _hiddenWord (string): a string of 5 underlines with space among them " "
       _letter (string): a string that contains a letter typed by the user.

    """
    def __init__(self):
        self._hiddenWord = ("_ " * 5) + "\n"
        self._letter =""

    def updateHiddenWord(self,word):
        if self._letter in word:
            index = word.index(self._letter)
            self._hiddenWord = self._hiddenWord[:(index*2)] + self._letter + self._hiddenWord[(index*2)+1:]
            return 1
        else:
            return 0
    def setHiddenWord(self,word):
        self._hiddenWord = word

    def setLetter(self, letter):
        self._letter = letter

    def getHiddenWord(self):
        return self._hiddenWord

        
