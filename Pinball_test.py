import random as rd

# 初始本金為100
capital = 100
print("你的起始彈珠數為:", capital,"顆")
for i in range(1000000):
    a = [2, 4, 6, 8, 10]
    # 隨機抽取2、4、6、8、10的倍率
    rate = rd.choice(a)  #本次倍率
    bet = 1  #測試中每次投入一顆彈珠
        
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
    if rd.random() <= hit_rate:
            capital += bet * rate
    else:
            capital -= bet

print("遊戲結束！你的最終本金為:", capital)
