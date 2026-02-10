# '''message = 'My new Python file!!'
# message = message + (str(10))
# print(message)
# '''

# # person_name = '   Aswani Jogi    '
# # message =  '"Want to learn python today \nyou can get into AI & ML space"'
# # print(person_name.lstrip()+ ' ' + message)

# # print(5 + 3)
# # print(12-4)
# # print(4*2)
# # print(round(72/9))

# people_for_dinner = ['Aswani','Suchitha','Shanvika','Keerthika']

# for people in people_for_dinner:
#     print(f"{people.upper()} invited for dinner by host")
#     if people == 'Aswani':
#         print(f"{people} can't make it due to personal emergency")
#         people_for_dinner.remove('Aswani')
#         people_for_dinner.append('AJ')
# for people in people_for_dinner:
#     print(f"{people.upper()} invited for dinner by host")
# people_for_dinner.insert(0,'BigBro')
# del people_for_dinner[len(people_for_dinner)-1]
# print(people_for_dinner)
# no_of_items = len(people_for_dinner)
# no_of_items = round(no_of_items/2)
# people_for_dinner.insert((no_of_items),'SmallBro')
# print(people_for_dinner)
# while len(people_for_dinner) > 2:
#     people_for_dinner.pop(0)
# print(len(people_for_dinner))
# print(people_for_dinner)
# # del people_for_dinner[0]
# people_for_dinner.clear()
# print(people_for_dinner)

# fav_places = ['eluru', 'hyderabad', 'pune', 'chennai', 'bangalore', 'kolkatta']
# # print(sorted(fav_places, reverse=True))
# # print(fav_places)
# # fav_places.remove('eluru')
# # print(fav_places)
# # fav_places.insert(0,'eluru')
# fav_places.sort(reverse=True)
# print(fav_places)
s = 0
for i in range(1,101):
    s += i
print(s)