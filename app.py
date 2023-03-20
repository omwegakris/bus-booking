def greet(first_name, last_name):
    return f"Hello mr {first_name} {last_name}"


message = greet("Felix", "Smith")
print(message)


def multiply(*numbers):
    total = 1
    for x in numbers:
        total *= x
    print(total)


multiply(4, 5, 6, 7, 8)
