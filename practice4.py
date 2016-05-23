class divisors:
    num_input = int(input("Enter a number: "))
    divisor_num = num_input;
    divisor_list = []
    while divisor_num >= 1:
        if num_input % divisor_num == 0:
            divisor_list.append(divisor_num)
            divisor_num = divisor_num - 1
        else:
            divisor_num = divisor_num - 1
    print(divisor_list)