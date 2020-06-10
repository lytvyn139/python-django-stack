#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 
    'last_name' : 'Jordan'},
    {'first_name' : 'John', 
    'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ 
    {'x': 10, 
    'y': 20} 
]

x[1][0] = 15
#print(x)

students[0]['last_name'] = "Bryant"
#print(students)

sports_directory['soccer'][0] = 'Andres'
#print(sports_directory)

z[0]['y'] = 30
#print(z)
##################################################################################################################################
#2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
#  For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(1, len(students)):
        print(f"Student #{i} first name: {students[i]['first_name']}, last name is - {students[i]['last_name']} ")
#iterateDictionary(students) 
# Student #1 first name: John, last name is - Rosales 
# Student #2 first name: Mark, last name is - Guillen 
# Student #3 first name: KB, last name is - Tonel 
##################################################################################################################################
#3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

no_namers = [
        {'name':  'user1', 'last' : 'last1'},
        {'name' : 'user2', 'last' : 'last2'},
        {'name' : 'user3', 'last' : 'last3'},
    ]

def iterateDictionary2(key_name, no_namers):
    # for i in range(len(no_namers)):
    #     print(no_namers[i][key_name])
    for studentObj in no_namers:
        if key_name in studentObj:
            print(studentObj[key_name])
        else:
            print('key doesnt exist, try another key')
            return false
iterateDictionary2('name',no_namers)
iterateDictionary2('last',no_namers)
# user1
# user2
# user3
# last1
# last2
# last3
##################################################################################################################################
#4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dictionary):
    for key, value in some_dictionary.items():
        print(f"{len(some_dictionary[key])} {key.upper():}")
        for item in some_dictionary[key]:
            print(item)
#printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon