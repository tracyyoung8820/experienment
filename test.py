import random

def guess_number():
    """
    猜数字游戏
    电脑随机生成一个1-100之间的数字，玩家有7次机会猜测
    """
    # 生成随机数字
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🎮 欢迎来到猜数字游戏！")
    print(f"我已经想了一个1-100之间的数字，你有{max_attempts}次机会来猜中它。")
    print("-" * 50)
    
    while attempts < max_attempts:
        try:
            # 获取玩家输入
            guess = int(input(f"第{attempts + 1}次猜测，请输入数字: "))
            
            # 检查猜测结果
            if guess < secret_number:
                print("📈 太小了，再大一点！")
            elif guess > secret_number:
                print("📉 太大了，再小一点！")
            else:
                print(f"🎉 恭喜你！猜对了！数字就是 {secret_number}！")
                print(f"你用了 {attempts + 1} 次就猜中了！")
                return
            
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"你还剩 {remaining} 次机会")
            print("-" * 30)
            
        except ValueError:
            print("❌ 请输入有效的数字！")
    
    # 如果机会用完还没猜中
    print(f"💔 游戏结束！正确的数字是 {secret_number}")
    print("下次加油！")

def main():
    """主函数"""
    while True:
        guess_number()
        
        # 询问是否再玩一次
        play_again = input("\n还想再玩一次吗？(y/n): ").lower()
        if play_again != 'y':
            print("👋 谢谢游玩，再见！")
            break
        print()

# 运行游戏
if __name__ == "__main__":
    main()
