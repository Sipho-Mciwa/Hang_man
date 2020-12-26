import display_HangMan
import get_words
import random_word
import hide_letters
import unhide_letters

def start_game():
    """
    This function calls all the functions required 
    to launch the program
    """
    words = get_words.words()
    word = random_word.get_random_word(words)
    private_word, index = hide_letters.hide(word)
    unhide_letters.game(word, private_word, index)
    


if __name__ == "__main__":
    start_game()