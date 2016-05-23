class string_lists:
    test_word = input("Enter a word: ")
    forward_list = []
    backward_list = []
    for letter in test_word:
        forward_list.append(letter)
    for letter in forward_list:
        backward_list.append(letter)
    backward_list.reverse()
    if forward_list == backward_list:
        print(test_word + " is a palindrome.")
    else:
        print(test_word + " is not a palindrome.")

    print(forward_list)
    print(backward_list)