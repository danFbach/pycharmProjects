
class GetName:
    count = 0
    name = input("Enter your name: ")
    age = input("Enter you age: ")
    repetition = int(input("Please enter another number just for fun. "))
    oneHundred = 2016 + (100 - int(age))
    while count < repetition:
        print("Your name is  " + name + ", you are " + age + " years old and will turn 100 in the year " + str(oneHundred) + ".")
        count += 1