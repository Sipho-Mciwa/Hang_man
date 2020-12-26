# Hang-man

### Features

* Prompts user for file name.
* If user simply presses Enter without a file name, a default file will be used instead.
* Reads all the words from the user-specified file.
* Selects one random word from a list of words
* Selects one random character from the random word,
and replaces the rest of the characters with an underscore.
* User is than prompted to guess the characters that are hidden.
* If the user's guess is incorrect, the amount of lives left is
displayed and a hang-man is also displayed.
* If the user's guess is correct the word is updated, meaning
the underscore is replaced with that character
* If there are more than one type of character, and the user
guess that character correctly, all the underscores that previously replaced the character will be replace at the same time.
* User cannot input more than one character at a time.
* User can stop the program by typing either 'quit' or 'exit'
* The program has a folder "/tests" which has unittests for the functions used.

### To Run

* `python Hang_man.py`
* follow the input prompts to get the desired output

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific function's unittest, e.g hide_letters(): `python3 -m unittest tests.test_main.MyTestCase.test_hide_letters`


### Future improvements

* The user should be able to choose a level of diffculty, and if user chooses an 'Easy'
diffculty, the program should be able to increase the level if the user guesses a certain
amount of words correctly without losing lives
* Add longer words for a higher difficulty.