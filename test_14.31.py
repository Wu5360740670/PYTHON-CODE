"""name="itheima is a brand of itcast"
sum=0
for n in name:
    if n=='a':
        sum+=1
print(sum)"""#求a的个数
"""#有几个偶数
num=int(input("请输入数字："))
m=0
for n in range(1,num):
    if n%2==0:
        m+=1
print(f"从(1,{num}）里，有{m}个偶数")"""
#9*9

"""for n in range(1,10):
    for m in range(1,n+1):
        print(f"{m}*{n}={n*m}\t",end='')
    print("\n")"""
        
#发工资

n=1#员工编号
m=0#绩效
rmb=10000#余额
for i in range(1,21):
    import random
    m=random.randint(1,10)
    if m<5:
        print(f"员工{i}绩效分{m},不满足，不发工资，下一位")
        continue
    else:
        print(f"员工{i}绩效分{m},满足绩效分，发工资")
        rmb-=1000
        if rmb==0:
        break
    

