#Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list

my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
di={}
se=set(my_list)
for i in se:
    di[i]=my_list.count(i)

print(di)