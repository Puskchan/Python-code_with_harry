a = int(input("Enter a number: "))
for i in range(a):
    print("   "*(a-i-1), end="")
    print(" * "*(2*i+1), end="")
    print("   "*(a-i-1))