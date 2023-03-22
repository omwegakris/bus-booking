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


def save_user(**user):
    print(user["name"])
    print(user["id"])
    print(user["age"])


save_user(id=5451, name="Omwega", age="14")

letters = ["a", "b", "c", "d", "e", "f"]

letters[0] = "A"
print(letters)
// comment
