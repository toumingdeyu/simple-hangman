import string
class Word(object):
    '''
    Word object to store the attributes of a new hangman round

    '''
    def __init__(self, word):
        self.word = word
        # render helper
        self.letters = '_ '*(len(self.word))
        self.life = 10
        # remaining unrevealed letters
        self.remains = len(self.word)
        # guesses history
        self.used = ''
        self.inputWarning = ''

    def reveal(self, l):
        '''
        l(char): character guesses
        returns: the updated object
        '''
        if l not in list(string.ascii_letters):
            self.inputWarning = '{0} is not a letter, try again!'.format(l)
            return self
        l = l.lower()
        if l not in self.used:
            self.inputWarning = ''
            # update guesses history
            self.used += l
            if l not in self.word:
                self.life -= 1

            # update render helper
            new_letters = ''
            for i in range(len(self.letters)):
                if i%2 == 0 and self.word[i/2] == l:
                    new_letters += l
                    self.remains -= 1
                else:
                    new_letters += self.letters[i]
            self.letters = new_letters
        else:
            self.inputWarning = '{0} is already guessed, try again!'.format(l)
        return self
