import random

# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"


def welcome():
    print("---------------------------------------")
    print("-     中国工商银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")


# 银行的开户逻辑
def bank_addUser(account, account_type, username, password, country, province, street, door, money):
    if len(bank) > 100:
        return 3
    if account_type != "1" and account_type != "2":
        return 4

    if username in bank:
        return 2

    # 正常开户
    bank[account] = {
        "account": account,
        "username":username,
        "account_type": account_type,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1



# 开户的输入数据
def addUser():
    username = input("请输入姓名：")
    print("1类账户【金卡】：最大转账额为5万，转出最大5万，转入没限制")
    print("2类账户【普通卡】：最大转账额为2万，转出最大2万，转入没限制")
    print("选择1类账户请输入“1”，选择2类账户请输入“2”")

    account_type = input("请输入账户类型：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")
    door = input("请输入您家门牌号：")

    money = int(input("请输入初始化您的银行卡余额："))

    account = random.randint(10000000, 99999999)
    account = str(account)

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
        print(info % (username, account, account_type, password, country, province, street, door, money, bank_name))
        print(bank)

# 存钱
def cunqianadd(account):
    if account in bank:
        print("您的账户余额为：%d" % bank[account]["money"])
        money1 = int(input("请输入您存入的金额："))
        money = bank[account]["money"] + money1
        bank[account]["money"] = money
        return True
    else:
        return False


# 存钱的
def cunadd():
    account = input("请输入您的账号：")
    cun = cunqianadd(account)
    if cun == True:
        info = '''
                ------------个人账户信息------------
                账号:%s
                您的当前余额是：%s
        '''
        # 每个元素都可传入%
        print(info % (account, bank[account]["money"],))
    elif cun == False:
        print("账号不存在")


# 转账
def zhuanzhangadd(zhuanchu_accout, zhuanru_accout, password):
    if zhuanchu_accout in bank and zhuanru_accout in bank:
        if password == bank[zhuanchu_accout]["password"]:
            zhuanchu = int(input("请输入转账的金额："))
            if bank[zhuanchu_accout]["account_type"] == 1:
                print("您是1类账户，您的最大转账金额是50000。")
            elif zhuanchu > 50000:
                return 4
            if bank[zhuanchu_accout]["account_type"] == 2:
                print("您是2类账户，您的最大转账金额是20000。")
            elif zhuanchu > 20000:
                return 5
            money = bank[zhuanchu_accout]["money"] - zhuanchu
            if money >= 0:
                bank[zhuanchu_accout]['money'] = money
                return 0
            elif money < 0:
                return 3
        else:
            return 2
    else:
        return 1


# 转账的
def zhuanadd():
    zhuanchu_accout = input("请输入您要转出的账号：")
    zhuanru_accout = input("请输入您要转入的账号：")
    password = input("请输入您的用户密码：")
    zhuan = zhuanzhangadd(zhuanchu_accout, zhuanru_accout, password)
    if zhuan == 1:
        print("转出或转入的账号不存在")
    elif zhuan == 2:
        print("转出账户的密码输入错误")
    elif zhuan == 3:
        print("您的钱不够了，请您努力赚钱。")
    elif zhuan == 4:
        print("您是1类账户，您的最大转账金额不能超过50000。")
    elif zhuan == 5:
        print("您是2类账户，您的最大转账金额不能超过20000。")
    elif zhuan == 0:
        info = '''
               ------------个人账户信息------------
               用户名:%s               
               密码:%s
               账户类型:%s
               账户余额:%s
           '''
        print(info % (zhuanchu_accout, password, bank[zhuanchu_accout]["account_type"], bank[zhuanchu_accout]["money"]))


# 取钱
def withdrawaladd(accout, password):
    if accout in bank and password == bank[accout]["password"]:

        print("您的余额为%d" % bank[accout]["money"])

        money = bank[accout]["money"] - int(input("请输入您要取款的金额："))

        if money >= 0:
            bank[accout]["money"] = money
            return 0
        elif money < 0:
            return 3
    elif accout not in bank:
        return 1
    elif accout in bank:
        if password != bank[accout]["password"]:
            return 2


# 取钱的
def quqianadd():
    accout = input("请输入您的账号：")
    password = input("请输入您的密码：")
    quqian = withdrawaladd(accout, password)
    if quqian == 1:
        print("账号不存在")
    elif quqian == 2:
        print("密码输入错误")
    elif quqian == 3:
        print("账号余额不足")
    elif quqian == 0:
        info = '''
               ------------个人信息------------
               用户名:%s               
               密码：%s
               余额：%s
           '''
        # 每个元素都可传入%
        print(info % (accout, bank[accout]["password"], bank[accout]["money"]))


# 查询
def inquireadd(accout, password):
    if accout in bank and password == bank[accout]["password"]:
        return 1
    else:
        return 0


# 查询的
def chaxunadd():
    accout = input("请输入您的用户名：")
    password = int(input("请输入您的用户密码："))
    chaxun = inquireadd(accout, password)

    if chaxun == 1:
        print("账户信息不存在")
    elif chaxun == 2:
        print("密码输入错误")
    elif chaxun == 0:
        info = '''
                              ------------个人信息------------
                              用户名:%s
                              账户类型：%s
                              账号：%s
                              密码：%s
                              国籍：%s
                              省份：%s
                              街道：%s
                              门牌号：%s
                              余额：%s
                              开户行名称：%s
                          '''

        print(info % (accout, bank[accout]['account_type'], bank[accout]['account'], bank[accout]['password'],
                      bank[accout]['country'], bank[accout]['province'],
                      bank[accout]['street'], bank[accout]['door'], bank[accout]["money"], bank_name))


while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        cunadd()
    elif chose == "3":
        quqianadd()
    elif chose == "4":
        zhuanadd()
    elif chose == "5":
        chaxunadd()
    elif chose == "6":
        print("Bey!")
        break
