# Attempt to pull Dog word out of words variable...failed first time...then succeded so coming back to it and keeping it
class Game:
    
    def __init__(self,word):
        self.word = word

words = Game('Dog')

# print(words.word)YAY IT WORKED    


# tried something offline did not work in python3 game.py in terminal
    # def convert_letter():
    #     display_word_to_guess = words
    #     for i in range(0, len(words)):
    #         if ord(words[i]) != 8:
    #             display_word_to_guess = display_word_to_guess (words[i], '_ ')
    #         print(display_word_to_guess)

# next step would be to try regular expresions, but then have to use import re at top, thought that would be cheating so scratch that


# using len() function to find the length of the string, will input a loop probably later
    # def display_length_of_word (self):
    #     print(len(words))
    
    # def display_each_letterofword_as_underscore (self)


# Going to try to use same approach as word frequency hw
# import string 

# word_to_guess= 'Dog'
# nvm after talking with Brian I learned this code does not run the same in ipython in this terminal vs python3 game.py in computers terminal 
