import random

def generate_secret_number():
    # 生成一个三位数的秘密数字
    secret_number = random.sample(range(10), 3)
    return secret_number

def get_user_input():
    # 获取用户输入的猜测数字
    user_input = input("请输入一个三位数：")
    
    user_input = [int(digit) for digit in user_input]
    return user_input

def check_guess(secret_number, user_input):
    # 检查用户的猜测并给出相应的提示
    result = []
    for i in range(3):
        if user_input[i] == secret_number[i]:
            result.append("Fermi")
        elif user_input[i] in secret_number:
            result.append("Pico")
    if len(result) == 0:
        result.append("Bagels")
    return result

def play_game():
    secret_number = generate_secret_number()
    print(secret_number)
    attempts = 0
    while attempts < 10:
        user_input = get_user_input()
        attempts += 1
        result = check_guess(secret_number, user_input)
        print(result)
        if result == ["Fermi", "Fermi", "Fermi"]:
            print("你赢了！")
            return
    print("你输了！秘密数字是", secret_number)

play_game()
