import random

# 初始本金為100
capital = 100
print("你的起始彈珠數為:", capital,"顆")
a = [2, 4, 6, 8, 10]
while capital > 0:
# 隨機抽取2、4、6、8、10的倍率
    rate = random.choice(a)
    print("本次倍率為:", rate)

# 讓玩家決定要投入多少彈珠
    print("輸入0將會直接結束遊戲")
    if capital > 99:
        bet = int(input("請輸入投入彈珠的數量(小於等於99): "))
    else:
        bet = int(input("請輸入投入彈珠的數量(小於等於%d): " % capital))
    while bet > capital:
        bet = int(input("超過本金了喔，請重新輸入投入彈珠的數量(小於等於%d): " % capital))
    while bet > 99:
        bet = int(input("超過99了喔，請重新輸入投入彈珠的數量(小於等於99): "))
    if bet == 0:
        break
    
# 給不同倍率的命中率
    if rate == 2:
        hit_rate = 0.33
    elif rate == 4:
        hit_rate = 0.25
    elif rate == 6:
        hit_rate = 0.17
    elif rate == 8:
        hit_rate = 0.08
    else:
        hit_rate = 0.08

# 隨機決定是否命中
    if random.random() <= hit_rate:
        print("恭喜你命中了！")
        capital += bet * rate
    else:
        print("很遺憾，你沒有命中。")
        capital -= bet

# 輸出剩餘的本金
    print("剩餘本金為:", capital)

# 判斷是否繼續遊戲
    if capital <= 0:
        break

print("遊戲結束！你的最終本金為:", capital)
