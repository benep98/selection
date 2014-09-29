amount = int(input("Enter an amount of money"))
twenty = amount //20
remainder = amount % 20
ten = remainder // 10
remainder = remainder % 10
five = remainder // 5
remainder = remainder % 5
two = remainder // 2
remainder = remainder % 2
one = remainder // 1
remainder = remainder % 1

print("The amount of £20's is {0}".format(twenty))
print("The amount of £10's is {0}".format(ten))
print("The amount of £5's is {0}".format(five))
print("The amount of £2's is {0}".format(two))
print("The amount of £1's is {0}".format(one))
