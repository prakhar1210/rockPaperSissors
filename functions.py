# loops
# for loop
for i in [1, 2, 3, 4, 5]:
    if i==3:
        print('fizzzzz')
    elif i==5:
        print('buzzzz')


# new for loop 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for i in numbers:
    total = total + i
    print(total) 


    # strings

    strings = 'i love coding in python and it is a oops lang.'
    count = 0
    for i in strings:
        if i == 'o':
            count += 1

    print(count)

    nums = [3, 6, 9, 10, 12, 15, 18]
    def fizzbuzz(nums):
        for i in nums:
            if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5
                print("fizzbuzz")
            elif i % 3 == 0:  # Divisible by 3
                print("fizz")
            elif i % 5 == 0:  # Divisible by 5
                print("buzz")
            else:  # Not divisible by 3 or 5
                print(i)

    fizzbuzz(nums)


    squares = { x: x*x for x in range(6)}
    squares