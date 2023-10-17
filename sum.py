#while循环
"""i=1
sum=0

while i<=100:
    sum+=i
    i+=1
print("sum=%d"% sum)
print(f"sum={sum}")"""
#1-100用while循环猜数字
import random
num=random.randint(1,100)
guess_num=int(input("请输入数字："))
while guess_num==num:
    if guess_num>num:
        print("大了")
        guess_num=int(input("请重新输入数字："))
    else:
        print("小了")
        guess_num=int(input("请重新输入数字："))
    print("猜对了")
