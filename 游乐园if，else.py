a=int(input("输入A心中的数字："))
print("游戏开始，请B输入第一次猜想的数字：")
b=input()
for n in 3:
    if b==a:
        print("恭喜你，猜对了！！")
    elif b>a:
        print("不对，猜错了")
    elif b<a:
        print("不对，再猜一次")