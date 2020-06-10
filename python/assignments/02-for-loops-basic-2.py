#1. Biggie Size 
# Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]

# my_list = [-1, 3, 5, -5]
# def biggie_size(my_list):
#     for i in range(0, len(my_list)):
#         if my_list[i] < 0:
#             my_list[i] = "big"
#     return my_list
# print(biggie_size(my_list))

#2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# my_list = [1,6,-4,-2,-7,-2]
# def count_positives(my_list):
#     counter = 0
#     for i in range(0, len(my_list)):
#         if my_list[i] > 0:
#             counter +=1
#     print(len(my_list))
#     my_list.pop(len(my_list)-1)
#     my_list.append(counter)
#     #print(len(my_list))
#     return my_list
# print(count_positives(my_list))

#3. Sum Total - Create a function that takes a list and returns the sum of all 
# the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

my_list = [6,3,-2]
def sum_total(my_list):
    sum = 0
    for i in range(0, len(my_list)):
        sum +=my_list[i]
    return sum
print(sum_total(my_list))

#.4 Average 
# Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5

# my_list = [1,2,3,4]
# def avg(my_list):
#     sum = 0
#     for i in range(0, len(my_list)):
#         sum +=my_list[i]
#     return sum/len(my_list)
# print(avg(my_list))
    
# #5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# my_list = [37,2,1,-9]
# def get_list_length(my_list):
#     return len(my_list)
# print(get_list_length(my_list))
        
#6  Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
my_list = [37,2,1,-9]
def find_min(my_list):
    min = 0
    for i in range (0, len(my_list)):
        if my_list[i] < min:
            min = my_list[i]
    return min
print(find_min(my_list))

#7  Max
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

my_list = [37,2,1,-9]
def find_max(my_list):
    max = 0
    for i in range (0, len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max
print(find_max(my_list))

#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 
# 'average': 7.75, 
# 'minimum': -9, 
# 'maximum': 37, 
# 'length': 4 }
my_list = [37,2,1,-9]
def ultimate_analysis(arr):
    new_object = {}
    #grabbing the stuff from above
    new_object["sum_total"] = sum_total(arr)
    new_object["min"] = find_min(arr)
    new_object["max"] = find_max(arr)
    return new_object
print(ultimate_analysis(my_list))

#9Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# Reversing a list using reverse()
# my_list = [37,2,1,-9]
# def reverse_list(my_list):
#     return [ele for ele in reversed(my_list)] 
# print(reverse_list(my_list)) 

# # Reversing a list using reverse()
# my_list = [37,2,1,-9]
# def reverse_list(my_list):
#     my_list.reverse()
#     return my_list
# print(reverse_list(my_list)) 


