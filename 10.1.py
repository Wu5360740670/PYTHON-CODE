#0-100猜数字
i=1
import random
num=random.randint(1,100)
guess_num=int(input("请输入数字："))
while True:
    if guess_num>num:
        print("大了")
        guess_num=int(input("请重新输入数字："))
        i+=1
    elif guess_num<num:
        print("小了")
        guess_num=int(input("请重新输入数字："))
        i+=1
    else:
        print(f"猜对了,数字就是{guess_num}")
        break
print(f"一共猜了{i}次")