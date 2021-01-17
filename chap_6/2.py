a1 = int(input("Enter marks of subject 1 in %: "))
a2 = int(input("Enter marks of subject 2 in %: "))
a3 = int(input("Enter marks of subject 3 in %: "))

if (a1+a2+a3)/3 >= 40 and a1 > 33 or a2 > 33 or a3 > 33:
    print("This boy is passed")
else:
    print("My boi failed")
