# Write a program where the user is asked to enter two integers (divisor and dividend) and the quotient and the remainder of their division is computed.(Both divisor and dividend should be integers.)

divisor = int(input("enter a no: "))
dividend = int(input("enter a no: "))

reminder = divisor//dividend
quotient = divisor%dividend

print(reminder)
print(quotient)