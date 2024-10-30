def fizzbuzz(number):
    if (number % 15 == 0):
        return "FizzBuzz"
    elif (number % 5 == 0):
        return "Buzz"
    elif (number % 3 == 0):
        return "Fizz"
    else:
        return number

assert fizzbuzz(15) == "FizzBuzz", "Error: fizzbuzz(15) が 'FizzBuzz' を返しません．"
assert fizzbuzz(5) == "Buzz", "Error: fizzbuzz(5) が 'Buzz' を返しません．"
assert fizzbuzz(3) == "Fizz", "Error: fizzbuzz(3) が 'Fizz' を返しません．"
assert fizzbuzz(1) == 1, "Error: fizzbuzz(1) が 1 を返しません．"
