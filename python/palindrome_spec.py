# Can you translate this driver code to unit tests?

import unittest
from palindrome import palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome_words(self):
        self.assertTrue(palindrome('racecar'))
        self.assertTrue(palindrome('Noon'))
        self.assertTrue(palindrome('ciVic'))
        self.assertFalse(palindrome('nice'))
        self.assertTrue(palindrome(434))
        self.assertFalse(palindrome(123))
        self.assertFalse(palindrome('bomb'))

    def test_palindrome_sentences(self):
        self.assertTrue(palindrome('Sore was I ere I saw Eros.'))
        self.assertTrue(palindrome('A man, a plan, a canal -- Panama'))

if __name__ == '__main__':
    unittest.main()
#should any of these fail on purpose?