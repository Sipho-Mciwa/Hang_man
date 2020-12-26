
def choose_file():
    """
    This function prompts the user for the type (length)
    of words they wish to use in the program.
    """
    file_names = ["short", "mid", ""]
    print("***** Welcome to Hang-man! *****")
    user_Input = input("choose a file (short or mid) or press 'Enter' to use short_words: ")

    while (user_Input not in file_names):
        user_Input = input("choose a file between 'short' and 'mid' or press 'Enter' to use short instead: ")

    if len(user_Input) == 0:
        user_Input = "short_words.txt"
    else:
        user_Input = user_Input[:] + "_words.txt"
    return (user_Input)


def words():
    """
    This function uses the user's input to 
    retrive the file that has the type (length)
    of words the user chose.
    """
    file_name = choose_file()
    fwords = open(file_name, 'r')
    list = fwords.readlines()
    fwords.close()
    return list
