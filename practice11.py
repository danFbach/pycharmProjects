class primes:
    user_input = int(input("Enter a number to have checked. "))
    count = user_input - 1
    not_prime = False
    if user_input % 2 != 0:
        while not not_prime:
            if count == 1:
                print("Prime")
                break
            if user_input % count == 0:
                print("Not prime.")
                not_prime = True
            else:
                print(count)
                count -= 1
    else:
        print("Not Prime.")