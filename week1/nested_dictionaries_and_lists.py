# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]['last name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print (sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


# 2. Iterate Through a List of Dictionaries

def iterate_dictionary(students):
    for dictionary in students:
        for key, value in dictionary.items():
            print(f"{key} - {value}")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    

iterate_dictionary(students)


# 3. Get Values From a List of Dictionaries

def iterate_dictionary2(key, students):
    for dictionary in students:
        print(dictionary[key])
    
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values

def print_info(dojo):
    for key, value in dojo.items():
        print(f"{key} - {len(value)}")
        for value in value:
            print(value)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print_info(dojo)
