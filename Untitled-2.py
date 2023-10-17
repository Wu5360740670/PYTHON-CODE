import random
num=random.randint(1,10)
print("请开始游戏,你有3次机会。")
guess_num=int(input("输入你要猜测的数字："))
if guess_num==num:
    print("恭喜")
else:
    if guess_num>num:
        print("大了")
    else:
        print("小了")
    guess_num=int(input("输入第二次你要猜测的数字："))
if guess_num==num:
    print("恭喜你，猜对了")
else:
    if guess_num>num:
        print("大了")
    else :
        print("小了")
    guess_num=int(input("输入第三次你要猜测的数字："))
    if guess_num==num:
        print('恭喜你，最后一次机会猜对了')
    else:
        print("猜错了")
    print(f"猜错了，最终答案是{num}")
