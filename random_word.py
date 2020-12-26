import random

def get_random_word(words):
    """
    This function generates a random index
    that ranges based on the number words in
    a list, and uses that index to return the
    corresponding word of that index in a list.
    """
    index = random.randint(0, len(words) - 1)
    return(words[index])