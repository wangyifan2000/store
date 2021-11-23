import random
from DBUtils import update
from DBUtils import select

# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国农业银行昌平支行"


def welcome():
    print("---------------------------------------")
    print("-     中国农业银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")


# 银行的开户逻辑
def bank_addUser(account,account_type, username, password, country, province, street, door, money):
    # 判断是否已满
    sql = "select count(*) from user"
    param = []
    data = select(sql, param, mode="one")  # (4,)
    if data[0] > 100:
        return 3

    sql1 = "select * from user where username  = %s"
    param1 = [username]
    data1 = select(sql1, param1, mode="all")  # ()

    # 判断是否开过户
    if len(data1) > 0:
        return 2
    if account_type != "1" and account_type != "2":
        return 4

    # 正常开户
    sql2 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,account_type, username, password, country, province, street, door, money, "2021-11-22", bank_name]
    update(sql2, param2)
    return 1


# 开户的输入数据
def addUser():
    username = input("请输入姓名：")
    print("1类账户【金卡】：最大转账额为5万，转出最大5万，转入没限制")
    print("2类账户【普通卡】：最大转账额为2万，转出最大2万，转入没限制")
    print("选择1类账户请输入“1”，选择2类账户请输入“2”")
    account_type = input("请输入账户类型:")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")
    door = input("请输入您家门牌号：")

    money = int(input("请输入初始化您的银行卡余额："))

    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, account_type, username, password, country, province, street, door, money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 4:
        print("您输入的账户类型无效")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            账户类型：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username, account,account_type, password, country, province, street, door, money, bank_name))
        print(bank)
#存钱
def Save_money():
    # 判断用户是否存在
    username = input("请输入用户名:")

    sql1 = "select * from user where username  = %s"
    param1 = [username]
    data1 = select(sql1, param1, mode="all")  # ()
    if len(data1) > 0:
        money1 = input("请输入存入的金额:")#存入金钱
        sql2 = "update user set money =money +%s where username;"
        param2 = money1
        update(sql2, param2)
        print("恭喜您存款成功")
    else:
        print("用户名不存在，请您前往开户。")
#取钱
def Withdraw_money():
    #判断用户是否存在
    username1 = input("请输入用户名:")

    sql1 = "select * from user where username  = %s"
    param1 = [username1]
    data1 = select(sql1, param1, mode="all")  # ()
    if len(data1) > 0:
        password1 = input("请输入密码:")




while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        Save_money()
    elif chose == "3":
        pass
    elif chose == "4":
        pass
    elif chose == "5":
        pass
    elif chose == "6":
        pass
