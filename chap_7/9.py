a = int(input("Enter a number: "))
print(" * "*a)
for i in range(a-2):
    print(" * ",end="")
    print("   "*(a-2),end="")
    print(" * ",)
    # pass
print(" * "*(a))