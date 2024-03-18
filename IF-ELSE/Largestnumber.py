#Write a Program to Find Largest Number Among Three Numbers entered by users

a = int(input("enter a no:"))
b = int(input("enter a no: "))
c = int(input("enter a no: "))

if a >b and a>c:
    print (a)
elif b>a and b>c:
    print (b)
else:
    print(c)