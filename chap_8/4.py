def sum(n):
    a=0
    for i in range(n):
        a = sum(n-1)+n
    return a

print(sum(2))