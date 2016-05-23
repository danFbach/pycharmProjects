class fibonacci:
    count = 0
    current = 1
    a = [1]
    limit = int(input("Enter a limit to the Fibbonnaci sequence. "))
    while count < limit:
        a.append(current)
        current = current + a[count]
        count += 1
    print(a)