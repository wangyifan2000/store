'''
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
'''


class cup:
    height = 0  # 高度
    volume = 0  # 容积
    colour = ''  # 颜色
    Material = ''  # 材质

    def deposit(self):
        print('一个', self.height, "cm的水杯", "能存储", self.volume, "ml的液体，水杯是", self.colour, "的，", self.Material, "的。")


a = cup()
a.height = 15
a.volume = 300
a.colour = "蓝色"
a.Material = "玻璃"
a.deposit()
