
# 1. Write another script that prints the double of all values between 4 and 8(exclusive) on the list [1,2,3,4,5,6,7,8,9]
mylist=[1,2,3,4,5,6,7,8,9]

for n in mylist:
    if n > 3 and n < 9:
        n = n*2
        print(n)

# 2. Write another Python script that separates all values in the list [1,2,3,4,5,6,7,8,9] in two other lists.
# One resulting list should contain all even numbers and the other should contain all odd numbers.
listeven = []
listodd = []

for n in mylist:
    if (n%2 ==0):
        listeven.append(n)
    else:
        listodd.append(n)

print(listodd)
print(listeven)

# 3. A script that prints the integers from 1 to 100.
# For multiples of three print “Fizz” instead , and
# for the multiples of five print “Buzz”.
# For numbers which are multiples of both print “FizzBuzz”

hundred = list(range(101))

for n in hundred:
    if (n ==0):
        print('Numbers')
    elif (n%3 == 0) and (n%5 == 0):
        print('FizzBuzz')
    elif (n%5 == 0):
            print('Buzz')
    elif (n%3 == 0):
        print ('Fizz')
    else:
        print(n)