first_number = int(input("Please enter your first number"))
second_number = int(input("Please enter your second number"))

answer = first_number // second_number
answer2 = first_number % second_number


print("{0} divides by {1} a number of {2} times".format(first_number,second_number,answer))
print("The remainder of {0} divided by {1} is {2}".format(first_number,second_number,answer2))
