import palindrome
import unittest


class PalindromeTests(unittest.TestCase):
    def test_true_empty(self):
        self.assertTrue(palindrome.is_palindrome(""))

    def test_true_whitespace(self):
        self.assertTrue(palindrome.is_palindrome(" "))
        self.assertTrue(palindrome.is_palindrome("      "))
        self.assertTrue(palindrome.is_palindrome("\n"))

    def test_true_number(self):
        self.assertTrue(palindrome.is_palindrome("1"))
        self.assertTrue(palindrome.is_palindrome("11"))

    def test_true_eng_char(self):
        self.assertTrue(palindrome.is_palindrome("a"))
        self.assertTrue(palindrome.is_palindrome("A"))
        self.assertTrue(palindrome.is_palindrome("aa"))
        self.assertTrue(palindrome.is_palindrome("AA"))
        self.assertTrue(palindrome.is_palindrome("aA"))
        self.assertTrue(palindrome.is_palindrome("aa a"))

    def test_true_rus_char(self):
        self.assertTrue(palindrome.is_palindrome("п"))
        self.assertTrue(palindrome.is_palindrome("пП"))
        self.assertTrue(palindrome.is_palindrome("п П "))

    def test_true_eng_phrase(self):
        self.assertTrue(palindrome.is_palindrome("Madam, I’m Adam"))

    def test_true_rus_phrase(self):
        self.assertTrue(palindrome.is_palindrome("Нам сила — талисман."))

    def test_true_eng_rus_char(self):
        self.assertTrue(palindrome.is_palindrome("aАa"))

    def test_false_eng_char(self):
        self.assertFalse(palindrome.is_palindrome("jk"))
        self.assertFalse(palindrome.is_palindrome("jK"))

    def test_false_rus_char(self):
        self.assertFalse(palindrome.is_palindrome("пр"))
        self.assertFalse(palindrome.is_palindrome("п р"))
        self.assertFalse(palindrome.is_palindrome("пР"))

    def test_false_eng_rus_char(self):
        self.assertFalse(palindrome.is_palindrome("aа"))
        self.assertFalse(palindrome.is_palindrome("аA"))


if __name__ == '__main__':
    unittest.main()
