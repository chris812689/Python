# answer = [[i for i in range(0,10)] for i in range(1,11)]
# print(answer)

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# total_donations=0
# for donations in donations.values():
#     total_donations += donations

# print(total_donations)

# This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# foods = ["gummy bears", "morning bun"]



# if food in bakery_stock:
#     print("{} left".format(bakery_stock[food]))    
# else:
#     print("We don't make that")


inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = {}
stock_list.update(inventory)

# add the value 18 to stock_list under the key "cookie"
stock_list.update({'cooke': 18})


# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")
print(stock_list)