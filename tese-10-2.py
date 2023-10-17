# def my_len(date):
#     n=0
#     for i in date:
#         n+=1
#     print(n)
# a="aadjdicjdiwe"
# my_len(a)

#t\体温
# def t(a):
#     if a<=37.5:
#         print(f'欢迎来到黑马程序员！请出示健康码和72小时核酸证明！并配合体温测量。正在测量体温，您的体温是{a}度，体温正常，请进！')
#     else:
#         print(f'欢迎来到黑马程序员！请出示健康码和72小时核酸证明！并配合体温测量。正在测量体温，您的体温是{a}度，体温不正常，请出去！')
# t(38)

#定义函数,说明文档
# def add(x,y):
#     """_summary_

#     Args:
#         x (_type_): _description_
#         y (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     result=x+y
#     print(f'{x}+{y}={result}')
#     return result
# add(1,2)


#局部变量和全局变量
# num=200
# def a():
#     print(f'a:{num}')
# def b():
#     num=500
#     print(f'b:{num}')
# a()
# b()
# print(num)

# num=200
# def a():
#     print(f'a:{num}')
# def b():
#     global num
#     num=500
#     print(f'b:{num}')
# a()
# b()
# print(num)





# #ATM
# money=5000000
# name=None
# #输入名字
# name=input("请输入真实姓名：")
# #查询余额函数
# def view():
#     print("...........查询余额...........")
#     print("姓名\t\t余额")
#     print(f'{name}\t\t{money}')
# #存款函数
# def deposit(num):
#     global money
#     money+=num
#     print("...........存款...........")
#     print("姓名\t存款\t余额")
#     print(f"{name}\t{num}\t{money}")
# #取款函数
# def withdrawal(num):
#     global money
#     money-=num
#     if money<0:
#         print("超出余额，无法取款")
#         money+=num
#     else:
#         print("...........取款...........")
#         print("姓名\t取款\t余额")
#         print(f"{name}\t{num}\t{money}")
    
# #主菜单函数
# def menu():
#     print("...........主菜单...........")
#     print(f"{name}，欢迎来到某某银行。请选择操作：")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入您的选择：")
# #永远循环
# while True:
#     key=menu()
#     if key=='1':
#         view()
#         continue
#     if key=='2':
#         a=int(input("请输入存款数目："))
#         deposit(a)
#         continue
#     if key=='3':
#         b=int(input("请输入取款数目："))
#         withdrawal(b)
#         continue
#     if key=='4':
#         print("请等待，正在退出")
#         break
#     else:
#         print("！！！！请输入正确的数字：")
#         continue
        
        
        
    





