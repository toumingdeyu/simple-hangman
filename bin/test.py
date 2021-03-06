import unittest
from hangman import word

class TestWordMethods(unittest.TestCase):
    def test_input_again(self):
        w1 = word.Word('abcde')
        w1.reveal('a')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('a')
        self.assertEqual(w1.inputWarning, '{0} is already guessed, try again!'.format('a'))
        w1.reveal('q')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('q')
        self.assertEqual(w1.inputWarning, '{0} is already guessed, try again!'.format('q'))

    def test_input_notletter(self):
        w1 = word.Word('abcde')
        w1.reveal('a')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('ab')
        self.assertEqual(w1.inputWarning, '{0} is not a letter, try again!'.format('ab'))
        w1.reveal('q')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('1')
        self.assertEqual(w1.inputWarning, '{0} is not a letter, try again!'.format(1))

    def test_input_correct(self):
        w1 = word.Word('abcde')
        w1.reveal('a')
        self.assertEqual(w1.life, 10)
        self.assertEqual(w1.letters, 'a _ _ _ _ ')
        self.assertEqual(w1.remains, 4)
        self.assertEqual(w1.used, 'a')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('b')
        self.assertEqual(w1.life, 10)
        self.assertEqual(w1.letters, 'a b _ _ _ ')
        self.assertEqual(w1.remains, 3)
        self.assertEqual(w1.used, 'ab')
        self.assertEqual(w1.inputWarning, '')
        w2 = word.Word('bbcaa')
        w2.reveal('a')
        self.assertEqual(w2.life, 10)
        self.assertEqual(w2.letters, '_ _ _ a a ')
        self.assertEqual(w2.remains, 3)
        self.assertEqual(w2.used, 'a')
        self.assertEqual(w2.inputWarning, '')
        w2.reveal('b')
        self.assertEqual(w2.life, 10)
        self.assertEqual(w2.letters, 'b b _ a a ')
        self.assertEqual(w2.remains, 1)
        self.assertEqual(w2.used, 'ab')
        self.assertEqual(w2.inputWarning, '')

    def test_input_wrong(self):
        w1 = word.Word('abcde')
        w1.reveal('g')
        self.assertEqual(w1.life, 9)
        self.assertEqual(w1.letters, '_ _ _ _ _ ')
        self.assertEqual(w1.remains, 5)
        self.assertEqual(w1.used, 'g')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('b')
        self.assertEqual(w1.life, 9)
        self.assertEqual(w1.letters, '_ b _ _ _ ')
        self.assertEqual(w1.remains, 4)
        self.assertEqual(w1.used, 'gb')
        self.assertEqual(w1.inputWarning, '')
        w2 = word.Word('bbcaa')
        w2.reveal('a')
        self.assertEqual(w2.life, 10)
        self.assertEqual(w2.letters, '_ _ _ a a ')
        self.assertEqual(w2.remains, 3)
        self.assertEqual(w2.used, 'a')
        self.assertEqual(w2.inputWarning, '')
        w2.reveal('g')
        self.assertEqual(w2.life, 9)
        self.assertEqual(w2.letters, '_ _ _ a a ')
        self.assertEqual(w2.remains, 3)
        self.assertEqual(w2.used, 'ag')
        self.assertEqual(w2.inputWarning, '')

    def test_win(self):
        w1 = word.Word('ab')
        w1.reveal('a')
        self.assertEqual(w1.life, 10)
        self.assertEqual(w1.letters, 'a _ ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'a')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('b')
        self.assertEqual(w1.life, 10)
        self.assertEqual(w1.letters, 'a b ')
        self.assertEqual(w1.remains, 0)
        self.assertEqual(w1.used, 'ab')
        self.assertEqual(w1.inputWarning, '')

        w2 = word.Word('bbcaa')
        w2.reveal('a')
        self.assertEqual(w2.life, 10)
        self.assertEqual(w2.letters, '_ _ _ a a ')
        self.assertEqual(w2.remains, 3)
        self.assertEqual(w2.used, 'a')
        self.assertEqual(w2.inputWarning, '')
        w2.reveal('b')
        self.assertEqual(w2.life, 10)
        self.assertEqual(w2.letters, 'b b _ a a ')
        self.assertEqual(w2.remains, 1)
        self.assertEqual(w2.used, 'ab')
        self.assertEqual(w2.inputWarning, '')
        w2.reveal('q')
        self.assertEqual(w2.life, 9)
        self.assertEqual(w2.letters, 'b b _ a a ')
        self.assertEqual(w2.remains, 1)
        self.assertEqual(w2.used, 'abq')
        self.assertEqual(w2.inputWarning, '')
        w2.reveal('c')
        self.assertEqual(w2.life, 9)
        self.assertEqual(w2.letters, 'b b c a a ')
        self.assertEqual(w2.remains, 0)
        self.assertEqual(w2.used, 'abqc')
        self.assertEqual(w2.inputWarning, '')
    def test_lose(self):
        w1 = word.Word('ab')
        w1.reveal('q')
        self.assertEqual(w1.life, 9)
        self.assertEqual(w1.letters, '_ _ ')
        self.assertEqual(w1.remains, 2)
        self.assertEqual(w1.used, 'q')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('b')
        self.assertEqual(w1.life, 9)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qb')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('w')
        self.assertEqual(w1.life, 8)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbw')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('e')
        self.assertEqual(w1.life, 7)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwe')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('r')
        self.assertEqual(w1.life, 6)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwer')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('t')
        self.assertEqual(w1.life, 5)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwert')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('y')
        self.assertEqual(w1.life, 4)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwerty')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('u')
        self.assertEqual(w1.life, 3)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwertyu')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('i')
        self.assertEqual(w1.life, 2)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwertyui')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('o')
        self.assertEqual(w1.life, 1)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwertyuio')
        self.assertEqual(w1.inputWarning, '')
        w1.reveal('p')
        self.assertEqual(w1.life, 0)
        self.assertEqual(w1.letters, '_ b ')
        self.assertEqual(w1.remains, 1)
        self.assertEqual(w1.used, 'qbwertyuiop')
        self.assertEqual(w1.inputWarning, '')
if __name__ == '__main__':
    unittest.main()
