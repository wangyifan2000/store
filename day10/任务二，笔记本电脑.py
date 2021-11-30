'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公
'''


class laptop:
    screen = 0  # 屏幕
    money = 0  # 价格
    cpu_model = ""  # cpu型号
    memory = 0  # 内存大小
    ssd = 0  # 硬盘大小
    standby = 0  # 待机时长
    model = ''  # 电脑型号
    colour = ''  # 电脑颜色
    weight = 0  # 电脑重量

    def typewriting(self):
        print('我正在', self.screen, '英寸的电脑屏幕上打字，我一分钟能打800个字。')

    def geme(self):
        print('我正在用我的', self.colour, '的', self.model, ',', self.cpu_model, '处理器、', self.memory, 'G运行', self.ssd,
              'G的硬盘的笔记本玩消消乐。')

    def video(self):
        print('我正在用我花了', self.money, '元买的笔记本电脑，看熊出没。电脑的待机时长有', self.standby, '小时之久。')

    def work(self):
        print("我正在用有", self.weight, '公斤重量的笔记本电脑敲代码。')


a = laptop()
a.screen = 15.6
a.money = 8888
a.cpu_model = 'i9-12990HK'
a.memory = 64
a.standby = 72
a.ssd = 528
a.model = '拯救者y100000'
a.colour = '白色'
a.weight = 2.5
a.typewriting()
a.geme()
a.video()
a.work()
