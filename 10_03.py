# a=[[1,2,3],[4,5,6]]
# print(a[1][1])
# mylist=["itcalst","ithrcima","python"]
# print(mylist.index("itcalst"))
# #超出就报错
# # print(mylist.index("halo"))
# mylist[0]="中国"
# print(mylist[0])
# mylist.insert(1,"best")
# print(f"结果：{mylist}")


# mylist=["I",'LOVE','YOU','I']
# # mylist.append('WUTAIZHONG')加一个
# # mylist.extend(["吴泰忠",'dangs'])加一组
# # del mylist[1]删除
# # mylist.pop(1)提出来
# # mylist.remove('I')重前到后检索
# # mylist.clear()清空
# # print(mylist.count('I'))统计元素
# # print(len(mylist))统计总元素个数
# print(f'我想表达的是：{mylist}')
#作业
# mylist=[21,25,21,23,22,20]
# mylist.append(31)
# print(f'列表mylist的内容为：{mylist}')
# mylist.extend([29,33,30])
# print(f'列表mylist的内容为：{mylist}')
# a=mylist.pop(0)
# b=mylist.pop(-1)
# c=mylist.index(31)
# print(a,b,c)


#作业
# list=[1,2,3,4,5,6,7,8,9,10]
# a=0
# new_list=[]
# # while a<len(list):
# #     if list[a]%2==0:
# #         new_list.append(list[a])
# #     a+=1
# # print(f'这列表{list}中，偶数项组成的列表为：{new_list}')
# for a in len(list):
#     if a%2==0:
#         new_list.append(list[a])
# print(new_list)

#元组
# tuple=('周杰伦','11',['football','music'])
# a=tuple.index('11')
# b=tuple[0]
# tuple[2][0]='coding'
# print(a,b,tuple)


#序列
# my_list=[0,1,2,3,4,5,6]
# print(my_list[1:4:1])
# my_tuple=(0,1,2,3,4,5,6)
# print(my_tuple[::])
# my_str="01234567"
# print(my_str[::2])
# print(my_str[::-1])#反转
# print(my_list[3:1:-1])

#倒序

# my_str="万过薪月,员序程马黑来,nohyp学"
# my_new_str=my_str[9:4:-1]
# print(my_new_str)

# my_new_str1=my_str[::-1]
# my_new_str2=my_new_str1[8:13:1]
# print(my_new_str2)

# my_list=my_str.split(",")
# print(my_list)
# my_new_str3=my_list[1]
# print(my_new_str3)
# my_new_str4=my_new_str3.replace("来",'')
# print(my_new_str4)
# my_new_str5=my_new_str4[::-1]
# print(my_new_str5)


