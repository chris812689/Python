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

class Counter:
    def __init__(self,low,high):
        self.low = low
        self.high = high
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.high:
            num = self.currrent 
            self.currrent += 1
            return num
        raise StopIteration

# def current_beat():
#     max = 100
#     nums = (1,2,3,4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i = 0
#         result.append(nums[i])
#         i +=1
#     return result

def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums) : i=0
        yield nums[i]
        i +=1
