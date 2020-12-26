import display_HangMan

def get_indices(word, user_Input, index_left):
    index = 0
    indices = []
    for letter in word:
        if (letter == user_Input and index != index_left):
            indices.append(index)
        index += 1
    return(indices) 


def do_update(word, private_word, user_Input, occurences):
    for item in (occurences):
        private_word = private_word[: item] + word[item] + private_word[item + 1: ]
    return (private_word)

        
def do_wrong(lives):
    print("You have", lives, "lives left.")
    print(display_HangMan.display(lives))


def game(word, private_word, index_left):
    print(private_word)
    user_Input = input("Guess the missing letters: ")
    lives = 5
    occurences = 0
    while (True):
        
        if (user_Input == "quit" or user_Input == "exit"):
            print("The word was:", word)
            break

        if(len(user_Input) == 1):

            if (user_Input in word):
                occurences = get_indices(word, user_Input, index_left)
                private_word = do_update(word, private_word, user_Input, occurences)
                print(private_word)
                if (private_word == word[:len(private_word)]):
                    print("You win!!!")
                    break
            else:
                lives -= 1
                do_wrong(lives)
                if (lives == 0):
                    print("Out of lives.\nThe word was:", word)
                    break
        else:
            print("One letter at a time.")
        user_Input = input("Guess the missing letters: ")
