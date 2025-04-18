# 1. Basic - Print all integers from 0 to 150.
for i in range(0,151):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001):
    if i % 5 == 0:
        print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000 and print the final sum.
total = 0
for i in range(1, 500001, 2):
    total += i
print(total)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter - Set three variables: low_num, high_num, mult. Starting at low_num and going through high_num, print only the integers that are a multiple of mult. For example, if low_num is 2, high_num is 9, and mult is 3, the loop should print 3, 6, 9 (on successive lines)
low_num = 1
high_num = 21
mult = 3
for i in range(low_num, high_num+1):
    if i % mult == 0:
        print(i)
