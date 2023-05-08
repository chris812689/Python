# def add_positive_numbers(x,y):
#     assert x>0 and y>0 , "Both numbers must be positive!"
#     return x+y

# print(add_positive_numbers(1,1))
# add_positive_numbers(1,-1)# Assertion Error: Both numbers must be positive!

def eat_junk(food):
    assert food in [
        "pizza", 
        "ice cream", 
        "candy", 
        "fried butter"
        ],"Food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"