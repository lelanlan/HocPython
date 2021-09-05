#Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
#Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
#vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []

sum=18
li=[]
A = [3, 6, 7, 9, 11, 12]
print(len(A))
for i in  range(0,len(A)):
    for j in range(i+1,len(A)):
        if (A[i]+A[j])==sum:
            li.append((A[i],A[j]))