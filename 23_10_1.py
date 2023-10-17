#99乘法表
# i=1

# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={j*i}\t",end='')
#         j+=1
#     i+=1
#     print("\n")
list=[1,2,3,4,5,6,7,8,9,10]
a=0
new_list=[]
while a<len(list):
    if list[a]%2==0:
        new_list.append(list[a])
    a+=1
print(f'这列表{list}中，偶数项组成的列表为：{new_list}')