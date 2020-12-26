import unittest
from unittest.mock import patch
from io import StringIO
import display_HangMan
import get_words
import random_word
import hide_letters
import Hang_man

class MyTestCase(unittest.TestCase):
    def test_display_HangMan_4_lives_left(self):
        self.assertEqual(display_HangMan.display(4),"""
/------------
|           |
|
|
|
|
-------------""")

    def test_display_HangMan_0_lives_left(self):
        self.assertEqual(display_HangMan.display(0),"""
/------------
|           |
|           0
|          /|\\
|           |
|          / \\
-------------""")

    def test_get_words(self):
        with patch('builtins.input', return_value="short"):
            self.assertEqual(get_words.words(), ['feed\n','feel\n','feet\n',
            'fell\n','find\n','fine\n','fire\n','first\n','fish\n','five\n','fix\n','flag\n',
        'floor\n','fly\n','food\n','foot\n','four\n','fox\n','from\n','full\n','funny\n'])


    def test_get_random_word(self):
        words = ['feed\n','feel\n','feet\n',
        'fell\n','find\n','fine\n','fire\n','first\n','fish\n','five\n','fix\n','flag\n',
        'floor\n','fly\n','food\n','foot\n','four\n','fox\n','from\n','full\n','funny\n']
        self.assertTrue(random_word.get_random_word(words) in words)
    

    def test_hide_letters(self):
        word = "feel\n"
        ans = hide_letters.hide(word)
        self.assertTrue("_" in ans[0])

        
if __name__ == "__main__":
    unittest.main()