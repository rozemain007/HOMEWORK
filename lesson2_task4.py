def fizz_buzz(n):
    for a in range(1,n):
        print(a)


    if (n % 3) == 0 and (n % 5) == 0:
        print("FizzBuzz")
    elif (n%5) == 0:
        print("Buzz")
    elif (n % 3) == 0:
        print("Fizz")




fizz_buzz(75)