class list_overlap:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 55, 9, 10, 11, 12, 13]
    c = []
    for num in a:
        if not c.__contains__(num):
            if b.__contains__(num):
                c.append(num)
    print(c)