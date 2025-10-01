def factorial(n):
    fact = 1
    while n != 0:
        fact = fact * n
        n -= 1
    return fact

# print(factorial(0))

def fibonacci(n):
    fib_list = [0,1]
    for i in range(1,n):
        new_item = fib_list[i] + fib_list[i-1]
        fib_list.append(new_item)
        print(f"new item:{new_item}, fib_list[i]:{fib_list[i]}, fib_list[i-1]:{fib_list[i-1]}, {fib_list}, thid is I cureently {i}")

    return fib_list[n]

print(fibonacci(4))

def fizzbuzz(n):

    fizzbuzz_list = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif i % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(i)


    return fizzbuzz_list

# print(fizzbuzz(15))