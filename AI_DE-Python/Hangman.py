import random as rd
from hangman_wordlist  import words
word_list = ['aswani','suchitha','shanvika','keerthika']

choosen_word = rd.choice(words)
print(choosen_word)
dep_count = len(choosen_word) + 5
for_count = 0 #len(choosen_word)
print(dep_count)
later_chosenword = []
delimiter = 0
flag_check = 0
read_first = 1 
for i in range(len(choosen_word)):
    later_chosenword.append('_')
print(later_chosenword)
while dep_count > 0:
    if flag_check == 1: break
    guess = input('Choose a letter from the word? \n')
    guess = guess.lower()
    for value in choosen_word:
        if guess == value:
            later_chosenword.pop(for_count)
            later_chosenword.insert(for_count,value)
            # dep_count -= 1
            for_count += 1
        else:
            for_count += 1
    read_first = 0
    dep_count -= 1 
    for_count = 0
    print(later_chosenword)
    if "_" not in later_chosenword:
        str_later_chosendword = map(str,later_chosenword)
        final_word = ''.join(str_later_chosendword)
        flag_check += 1
    delimiter = 0
print(final_word)


