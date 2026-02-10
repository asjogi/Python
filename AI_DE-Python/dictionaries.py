# travel_log = {
#     "France":{
#         "cities_visited":["Paris","Lille","Dijon"],
#         "total_visits":12
#     },
#     "Germany":["Berlin","Hamung","Stuttgart"],
# }
# print(travel_log["France"]["total_visits"])
# # nested_list = ["A","B",["C","D"]]
# # print(nested_list[2][1])
from auction_image import auction_logo as al
print(al)
print("Welcome to the secret auction program.")

name_of_participant = str(input("What is your name? : ")).title()
bid_value = int(input("What's your bid? : $"))

dic_for_bids = {}
other_bidders = True

def bidstoadd(name,value):
    dic_for_bids[name]= value


# print(dic_for_bids)

while other_bidders == True:
    bidstoadd(name_of_participant,bid_value)
    more_bidders = str(input("Do we have more bidders ? Yes or No :")).lower()
    if more_bidders == 'yes':
        print("\n"*50)
        name_of_participant = str(input("What is your name? : ")).title()
        bid_value = int(input("What's your bid? : $"))
        # print(dic_for_bids)
    else:
        other_bidders = False
        dic_for_bids = sorted(dic_for_bids.items(), key=lambda items: items[1])
print(f"Congratulations {dic_for_bids[0]}")