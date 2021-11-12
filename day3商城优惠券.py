'''
商城系统：
    列表：容器来存储数据
    for循环：遍历数据
    if...else：
1.技术选型：
2.需求
    1.准备一个货架，摆上很多商品
    2.准备一个空的购物车
    3.钱包还的有钱
    4.买东西
        1.如果有这个商品
            判断余额足够买这个东西
                够买
                    余额减去商品的价格
                    购物车添加这个商品
                    温馨提示：成功添加购物车！
                不够：
                    穷鬼，买啥？？？
                是否输入的是q或者Q:
                    退出！
        2.如果没有这个商品
            温馨：没有这个商品，别瞎弄！
    5.打印购物小条！
任务：10辣条优惠券（0.3），20机械革命优惠券（0.9）。
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
任务1：
    改造购物小条，将多条重复显示，优化成 yyyyyyy   xn
'''
import random
# 准备商品
import ko as ko

random1 = random.randint(0, 10)
random2 = random.randint(0, 20)
shop = [
    ["牙膏", 18],
    ["老年机", 350],
    ["豆瓣酱", 9.9],
    ["iphone 18 max pro", 15000],
    ["联想拯救者y10000k", 120000],
    ["可口可乐", 2.5],
    ["辣条", 3],
    ["机械革命", 8299],
]
# 定义一个空的购物车
mycart = []

# 定义优惠劵使用的次数
a = 0
b = 0
# 初始化自己的余额
salary = int(input("请输入您的余额："))
sal = salary
# 抽取优惠劵
print("恭喜您获得: %d 张辣条三折优惠劵，%d 张机械革命九折优惠劵" % (random1, random2))
while True:
    # 展示商品架
    for key, value in enumerate(shop):
        print(key, value)

    chose = input("请输入您要买的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose >= len(shop):
            print("温馨提示：这个商品不存在！别瞎弄！")
        else:
            if salary < shop[chose][1]:
                print("温馨提示：穷鬼，没钱，别瞎买！")
            else:
                if random1 > 0 and chose == 6:
                    random1 -= 1
                    print("辣条优惠劵剩余 %d 张，本次可使用三折优惠劵，原价3元 折后0.9元" % random1)
                    salary = salary-(shop[chose][1] * 0.3)
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                    a += 1
                elif random2 >= 1 and chose == 7:
                    random2 -= 1
                    print("机械革命优惠劵剩余 %d 张，本次可使用九折优惠劵，原价8299元 折后7469.1元" % random2)
                    salary = salary-(shop[chose][1] * 0.9)
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                    b += 1
                else:
                    salary = salary-shop[chose][1]
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("兄弟，商品不存在！别瞎弄！")

# 计算优惠金额
latiao = (3 - (3 * 0.3)) * a
jixiegeming = (8299 - (8299 * 0.9)) * b
ok = round(latiao, 2)
ko = round(jixiegeming, 2)
youhui = ok + ko

# 计算本次消费
xiaofei = (sal - salary)
xiaofei = round(xiaofei, 2)

# 打印购物小条
print("----------------欢迎下次光临小商店-------------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
print("您购买的商品有：")
m = []
for i in mycart:
    if i not in m:
        m.append(i)
        print(" %s x %s " % (i, mycart.count(i)))
    else:
        continue
print("--------------------------------------------------")
salary = round(salary, 2)
print("您本次消费为：￥", xiaofei, end=","),
print("剩余余额：￥%s" % salary)
print("本次消费使用辣条优惠劵 %d张 ，使用机械革命优惠劵 %d张" % (a, b))
print("累计为您节省了：￥", youhui)
