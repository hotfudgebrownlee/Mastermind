import random

class Board:
    """
    Stereotype: 
        Information Holder
    """
    def __init__(self):
        """The class constructor.
        Args:
            self (Board): an instance of Board.
        """
        self.code = 0
        self.currentGuess = 0
        self.hint = ''

    def get_code(self):
        self.code = random.randint(1000,9999)
        return self.code

    def apply(self, move, code):
        self.hint = ''
        currentGuess = list(str(move))
        trueCode = list(str(code))
        hintList = ['','','','']
        for i in range(4):
            if currentGuess[i] == trueCode[i]:
                hintList[i] = "x"
            elif currentGuess[i] in trueCode:
                hintList[i] = "o"
            else:
                hintList[i] = "*"
        for j in hintList:
            self.hint += j
        return self.hint

    def get_hint(self):
        return self.hint

    def matches_code(self):
        if self.get_hint() == 'xxxx':
            return True
        return False

"""TEST CASES"""
# x = Board()
# hint = x.apply(1234, 1304)
# print(hint)
# print(x.matches_code())