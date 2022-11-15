def sum_even_values(*args):
    total=0
    for num in args:      
        if num % 2 ==0:
            total += num
            
    return total


sum_even_values(1,2,3,4,5, 6 )