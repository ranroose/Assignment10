from module1 import find_two_smallest
from module2 import list1, list2, list3, list4, list5


lists_to_check = [list1, list2, list3, list4, list5]


with open("result.txt", "w") as result_file:
    for lst in lists_to_check:
        smallest_values = find_two_smallest(lst)
        result_file.write(f"The two smallest values in {lst} are: {smallest_values}\n")