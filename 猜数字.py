secret_number = 6
first_time = 0
last_time = 3
while first_time < last_time:
    try:
        number = int(input("Number: "))
        first_time += 1
        if number == secret_number:
            print("You won!")
            break
    except ValueError:
        print("Please type number")
else:
    print("You failed")