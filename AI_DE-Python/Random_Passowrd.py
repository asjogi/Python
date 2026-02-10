alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
]
import random
# print(random.sample(alphabets,5))
print('Welcome to password generator!!')

a_alphabets = int(input("How many alphabets do you want in your password ?\n"))
a_numbers = int(input("How many numbers do you want in your password ?\n"))
a_splcharacters = int(input("How many special characters do you want in your password ?\n"))
tot_alpha = ''
for a_alpha in random.sample(alphabets,(a_alphabets)):
    tot_alpha += str(a_alpha)
print(tot_alpha)

tot_num = ''
for a_num in random.sample(numbers,(a_numbers)):
    tot_num += str(a_num)

tot_splchars = ''
for a_splchars in random.sample(special_characters,(a_splcharacters)):
    tot_splchars += str(a_splchars)

print(((tot_alpha + tot_splchars + tot_num)))