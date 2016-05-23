class NumberCheck:
    num_to_check = int(input("Please enter a number "))

    if num_to_check % 4 == 0:
        print(str(num_to_check) + " is a multiple of 4")
    elif num_to_check % 2 == 0:
        print(str(num_to_check) + " is even.")
    else:
        print(str(num_to_check) + " is odd.")