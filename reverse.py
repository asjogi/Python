# import pandas as pd
# import numpy as np

# # a = np.arange(11,15)
# # series_1 = pd.Series(data=a, index=('a','b','c','d'))
# # print(np.dtype(series_1))


# # a = list(range(0,100,2))
# # gen = []
# # values_pr = [pr_list for pr_list in list(range(0,10,2)) if pr_list > 7]
# # print(values_pr)

# # print([i for i in range(1,10) if i%2==0])

# # a = list(range(0,100))
# # b = []
# """below piece of code is """
# # b = [1,2,3]
# # def run(a,c):
# #     b = []
# #     for i in a:
# #         if i%2 == 0:
# #             b.append(i)
# #     print((list(b)[0::2]))   
# # run(list(range(0,25)),26)
# # f = "Aswani Jogi"
# # q = (f[-1::-1])
# # w = str(reversed(f))
# # print(w)
# # if q == w :
# #     print('same')
# # result = ""
# # for i in f:
    
# #     print(i)
# #     result = i + result
# # print(result)
# # print(tuple(reversed(b)))

# """Convert list into a string"""
# # weekdays = ['mon','tues','wed','thur','frid','sat']
# # listasstring = '"'.join(weekdays)
# # print(list(reversed(weekdays)))
# """Sum of the numbers for a given number"""
# # num = 2000
# # tot = 0
# # while num > 0:
# #     listnum = num%10
# #     tot = listnum + tot
# #     num = num//10
# # print(tot)
# """Palindrome- Reversing a string should give same string"""
# # word = "malayalam"
# # inverse = word[::-1]
# # print(inverse)
# # if word == inverse:
# #     print("{} is a palindrome".format(word))
# # else:
# #     print("{} is not a palindrome".format(word))
# """Count capital letters"""
# """Add a value to python array"""
# # a = list(range(1,11))
# # a.remove(5)
# # print(a)
# # b = a.pop(-2)
# # print(a)

# word = "How Is It Going"
# count = sum(i.islower() for i in word)
# print(count)
# Aswani = 'HOWISITGOING'
# print(Aswani[-1::-1])
import random as r
 

friends = ["Aswani","Suchitha","Shanvika","Keerthika","Jogi","Kumar"]
print(friends[-1::-1])
# random_num = r.randint(0, (len(friends)-1))
# print(friends[random_num])
# print(r.choice(friends))
# tot_list = friends.copy()
# print(tot_list)



