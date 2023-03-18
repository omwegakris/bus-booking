temperature = 35

if temperature >= 35:
    print("Its hot outside")

temp_entry = input("Enter Temperature: ")

if int(temp_entry) >= 50:
    print("Your entry is high")
elif int(temp_entry) < 25:
    print("Its cool outside")
else:
    print("Its awesome outside")
