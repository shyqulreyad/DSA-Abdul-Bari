def rec(n):
    if n > 0:
        print(n)
        rec(n-1)

n= 4
# rec(n) 

def rec2(n):
    if n>0:
        rec2(n-1)
        print(n)
n=4
rec2(n)