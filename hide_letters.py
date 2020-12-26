import random

def hide(word):
    """
    This function replaces all letters in a random
    word with an underscore, but leaves one unhidden.
    e,g fine, will be returned as _i__, along
    with i's index.
    """
    new_word = "_"*(len(word) - 1)
    index = random.randint(0, len(word) - 2)
    new_word = new_word[:index] + word[index] + new_word[index + 1:]
    return (new_word, index)
