a1 = input("enter 1 number: ")
a2 = input("enter 2 number: ")
a3 = input("enter 3 number: ")
a4 = input("enter 4 number: ")

if a1 > a2 and a2 > a3 and a3 > a4:
    print(a1)
elif a2 > a3 and a3 > a4:
    print(a2)
elif a3 > a4:
    print(a3)
else:
    print(a4)