def whobig(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

print(whobig(999,880,120))