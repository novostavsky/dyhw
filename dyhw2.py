import random

file = "dict.txt"

#satndard print error
def print_error(letter):
    print("No luck, the letter {} is not in this word. Try again".format(letter))

#mask not guessed letters
def get_masked_word(word, guessed_letters):
    masked_word = ""
    for letter in  word:
        if letter in guessed_letters:
            masked_word = masked_word + letter
        else:
            masked_word = masked_word + '_'
    return masked_word

#check if the word is guessed
def is_guessed(word, guessed_letters):
    if "_" in get_masked_word(word, guessed_letters):
        return False
    else:
        return True

#get the word to guess
def get_word(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)

#let's roll
word = get_word(file)
guessed_letters = []
print(get_masked_word(word, guessed_letters))

num_tries = 0

while not is_guessed(word, guessed_letters):
    num_tries += 1
    c = input('Enter a character: ')
    if not c.isalpha():
        print(c + " - this is not a character, please try again...")
        break
    else:
        c = c.upper()
        print('the symbols is ' + c)
    if not c in word:
        print_error(c)
    else:
        guessed_letters.append(c)
    print(get_masked_word(word, guessed_letters))

print("Number of tries: {}".format(num_tries))