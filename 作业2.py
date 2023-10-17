import random
num =random.randint(100,999)
print(num)
# a=num//100#百位
# b=(num//10)%10#十位
# c=num%10#个位
# print(a,b,c)
str(num)
my_list=[]

m=0
while m<len(str(num)):
    if m==0:
        a=str(num)[0]
        m+=1
    if m==1:
        b=str(num)[1]
        m+=1
    if m==2:
        c=str(num)[2]
        m+=1
my_list=[a,b,c]
print(my_list)##验证答案，可以删除

# my_list=[]
# for i in num:
#     my_list.insert(i)
# print(my_list)
n=1
print("欢迎参加这个逻辑游戏，游戏规则如下：\n猜测一个三位字数字;\n对于你的猜测，游戏提供了以下提示之一: \n“ Pico”表示你的猜测数字有一个在正确数字里面，但位置不对; \n“ Fermi”表示你的猜测在正确的地方有一个正确的数字; \n“ Bagels”表示你的猜测没有正确的数字。\n你有10次机会猜这个秘密数字")
while True:
    get_num=int(input(f"游戏开始，请开始输入第{n}次的数字：\n"))
    my_get_list=[]
    l=0
    while l<len(str(num)):
        if l==0:
            a1=str(get_num)[0]
            l+=1
        if l==1:
            b1=str(get_num)[1]
            l+=1
        if l==2:
            c1=str(get_num)[2]
            l+=1
        my_get_list=[a1,b1,c1]
    # print(my_get_list)
    P=0
    B=0
    F=0
    if get_num<100 and get_num>1000:
        print("警告！报错！！请输入正确范围内的数字")
        continue
    if my_list==my_get_list:
        print("恭喜你，输入正确！！！！(*°▽°*)")
        break
    
    else:
        
        # for i in my_list:
        #     for p in my_get_list:
        #         if i==p:
        #             if my_list.index(i)==my_get_list.index(p):
        #                 F+=1
                        
        #             else:
        #                 P+=1    
        #         if i!=p:
        #             B+=1
        #             break
        #         if i==p:
        #             if my_list.index(i)==my_get_list.index(p):
        #                 F+=1
        #                 #print("Fermi")
        #                 break
                      
        #             else:
        #                 P+=1
        #                 #print("Pico")
        #                 break
        #         else:
        #             B+=1
        #             #print("Bagels")
        # if F>0 and P==0:
        #     print("fermi")
        # if P>0 and F==0:
        #     print("pico")
        # if B==3:
        #     print("bagels")
                    
        # for x in my_list:
        #     for y in my_get_list:
        #         if x==y:
        #             if m==l:
        #                 print("Fermi")
        #             else:
        #                 print("Pico")
        #         else:
        #             print("Begels")
    n+=1
    if n>10:
        break