# If number / 3, print fuzz. if number / 5, print buzz. if number / 3 and 5, print fizzbuzz for numbers 1 - 100

for number in range(1, 101):
    
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0: 
        print("Fizz")
    elif number % 5 == 0: 
        print("Buzz")
    else: 
        print(number)