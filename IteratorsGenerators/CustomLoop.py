# Customer For Loop

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("End of Iterator!")
            break

my_for("Christopher")