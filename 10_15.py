#字典
# score_dict={
#     "王力宏":{
#         "语文":77,"数学":66,"英文":33},"周杰伦":{"语文":88,"数学":86,"英文":55},"林俊杰":{"语文":99,"数学":96,"英文":66}
# }
# print(score_dict)
# print('周杰伦',score_dict['周杰伦'])

#新增/改变
# my_dict={"a":1,"b":2,"c":3}
# my_dict["a"]=4
# my_dict["d"]=10
# print(my_dict)
# print(my_dict.keys())


my_dict={
    
    'a':{"部门":"科技部","工资":3000,"级别":1 },
    'b':{"部门":"市场部","工资":5000,"级别":2 },
    'c':{"部门":"市场部","工资":7000,"级别":3 },
    'd':{"部门":"科技部","工资":4000,"级别":1 },
    'e':{"部门":"市场部","工资":6000,"级别":2 }
}
for key in my_dict:
    if my_dict[key]["级别"]==1:
        my_dict[key]["级别"]="2"
    my_dict[key]["工资"]=my_dict[key]["工资"]+1000
print(my_dict)



# def a():
#     return 1,2
# x,y=a()
# print(x,y)

# def a(b):
#     result=b(1,2)
#     print(result)
# def b(x,y):
#     return x+y
# a(lambda x,y:x+y)