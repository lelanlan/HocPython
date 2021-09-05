
n=4
#1
for i in range(1,n+1):
    sp= " "*(n-i)
    kt="*"*i
    print(sp+kt)
#2
for i in range(1,n+1):
    sp= " "*(n-i)
    kt="*"*i
    if i==n:
        kt = "*" * i*2
    print(sp+kt)
for i in range(1,n):
    sp= " "*n
    kt="*"*(n-i)
    print(sp+kt)
#3
for i in range(1,n+1):
    if 1<i<n:
     sp= "*"+" "*(i-2)+"*"
    elif i==1:
        sp="*"
    else:
        sp="*"*i*2
    print(sp)
for i in range(1,n):
    sp=" "*(n*2-(n-i))
    if n-i>2:
        kt= "*"+" "*(n-i-2)+"*"
    else:
        kt="*"*(n-i)
    print(sp+kt)