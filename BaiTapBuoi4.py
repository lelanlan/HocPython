from builtins import set

n=4
#b1
for i in range(1,n+1):
    sp= " "*(n-i)
    kt="*"*i
    print(sp+kt)
#b2
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
#b3
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
#b4
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
di={}
se=set(my_list)
for i in se:
    di[i]=my_list.count(i)
#b5
#unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}


#print(unique_value_dict)
#unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}
l=set()
lis_dict=([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])

for i in lis_dict:
    for j in i.values():
        l.add(j)

print(l)
print("=============================")
#b6
sum=18
li=[]
A = [3, 6, 7, 9, 11, 12]
print(len(A))
for i in  range(0,len(A)):
    for j in range(i+1,len(A)):
        if (A[i]+A[j])==sum:
            li.append((A[i],A[j]))


print(li)
