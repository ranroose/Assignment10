#Create a module. 
#The module has one function only: find_two_smallest(<list>). 
#The function receives a list of integers as a parameter and returns (not prints! returns!) two smallest list values. 
#The function prints nothing.

def find_two_smallest(list_of_integers):
    smallest = min(list_of_integers[0], list_of_integers[1])
    second_smallest = max(list_of_integers[0], list_of_integers[1])
    for num in list_of_integers[2:]:
        if num < smallest:
            second_smallest = smallest  
            smallest = num  
        elif num < second_smallest:
            second_smallest = num 
    return (smallest, second_smallest)

