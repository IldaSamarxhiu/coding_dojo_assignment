# 1. Countdown

number = int(input('Enter a number: '))

def countdown(number):
    result = []
    for num in range(number, -1, -1):
        result.append(num)
    return result

print(countdown(number))


# 2. Print and return

list_of_numbers = [int(x) for x in input('Enter two numbers separated by a space: ').split()]

def print_return(list_of_numbers):
    print(list_of_numbers[0])
    return list_of_numbers[1]

result = print_return(list_of_numbers)
print("Returned:", result)


# 3. First Plus Length

list_of_numbers = [int(x) for x in input('Enter some numbers separated by a space: ').split()]

def first_plus_length(list_of_numbers):
    return list_of_numbers[0] + len(list_of_numbers)

print(first_plus_length(list_of_numbers))


# 4. Values Greater than Second

list_of_numbers = [int(x) for x in input('Enter some numbers separated by a space: ').split()]

def values_greater_than_second(list_of_numbers):
    if len(list_of_numbers) < 2:
        return False
    
    second_value = list_of_numbers[1]
    
    new_list = [num for num in list_of_numbers if num > second_value]
    
    print(f"Number of values greater than the second value: {len(new_list)}")
    
    return new_list

print(values_greater_than_second(list_of_numbers))


# 5. This Length, That Value

def length_and_value(size, value):
    return [value] * size

print(length_and_value(4 ,7))
