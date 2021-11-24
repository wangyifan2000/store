import xlrd
#工作薄
wb = xlrd.open_workbook(filename=r"D:\python\保存位置\python\任务\day09\2020年每个月的销售情况.xlsx")
sheets = wb.sheet_names()
print(sheets)
# 全年销售总额
sum_age = 0
#全年销售总数量
total = 0
#商品
down_jacket = 0
jeans = 0
dust_coat = 0
fur = 0
T_shirt = 0
vest = 0
fur_clothing = 0
small_suits = 0
casual_pants = 0
Sweater = 0
shirt = 0
Cotton = 0
Pencil_pants = 0
down_jacket1 = 0
jeans1 = 0
dust_coat1 = 0
fur1 = 0
T_shirt1 = 0
vest1 = 0
fur_clothing1 = 0
small_suits1 = 0
casual_pants1 = 0
Sweater1 = 0
shirt1 = 0
Cotton1 = 0
Pencil_pants1 = 0
for i in range(wb.nsheets):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for j in range(1,rows):
        data = st.row_values(j)
        sum_age += data[2]*data[4]
    for x in range(1, rows):
        data1 = st.row_values(x)
        total += data1[4]
    for k in range(1,rows):
        data2 = st.row_values(k)
        if data2[1] == "羽绒服":
            down_jacket += data2[4]
            down_jacket1 += data2[4]*data2[2]
        elif data2[1] == "牛仔裤":
            jeans += data2[4]
            jeans1 += data2[4] * data2[2]
        elif data2[1] == "风衣":
            dust_coat += data2[4]
            dust_coat1 += data2[4] * data2[2]
        elif data2[1] == "皮草":
            fur += data2[4]
            fur1 += data2[4] * data2[2]
        elif data2[1] == "T血":
            T_shirt += data2[4]
            T_shirt1 += data2[4] * data2[2]
        elif data2[1] == "马甲":
            vest += data2[4]
            vest1 += data2[4] * data2[2]
        elif data2[1] == "皮衣":
            fur_clothing += data2[4]
            fur_clothing1 += data2[4] * data2[2]
        elif data2[1] == "小西装":
            small_suits += data2[4]
            small_suits1 += data2[4] * data2[2]
        elif data2[1] == "休闲裤":
            casual_pants += data2[4]
            casual_pants1 += data2[4] * data2[2]
        elif data2[1] == "卫衣":
            Sweater += data2[4]
            Sweater1 += data2[4] * data2[2]
        elif data2[1] == "衬衫":
            shirt += data2[4]
            shirt1 += data2[4] * data2[2]
        elif data2[1] == "棉衣":
            Cotton += data2[4]
            Cotton1 += data2[4] * data2[2]
        elif data2[1] == "铅笔裤":
            Pencil_pants += data2[4]
            Pencil_pants1 += data2[4] * data2[2]
#一月份
January = wb.sheet_by_index(0)
rows = January.nrows
total1 = 0
down_jacket2 = 0
jeans2 = 0
dust_coat2 = 0
fur2 = 0
T_shirt2 = 0
vest2 = 0
fur_clothing2 = 0
small_suits2 = 0
casual_pants2 = 0
Sweater2 = 0
shirt2 = 0
Cotton2 = 0
Pencil_pants2 = 0
for a1 in range(1, rows):
    data2 = January.row_values(a1)
    total1 += data2[4]
    if data2[1] == "羽绒服":
        down_jacket2 += data2[4]
    elif data2[1] == "牛仔裤":
        jeans2 += data2[4]
    elif data2[1] == "风衣":
        dust_coat2 += data2[4]
    elif data2[1] == "皮草":
        fur2 += data2[4]
    elif data2[1] == "T血":
        T_shirt2 += data2[4]
    elif data2[1] == "马甲":
        vest2 += data2[4]
    elif data2[1] == "皮衣":
        fur_clothing2 += data2[4]
    elif data2[1] == "小西装":
        small_suits2 += data2[4]
    elif data2[1] == "休闲裤":
        casual_pants2 += data2[4]
    elif data2[1] == "卫衣":
        Sweater2 += data2[4]
    elif data2[1] == "衬衫":
        shirt2 += data2[4]
    elif data2[1] == "棉衣":
        Cotton2 += data2[4]
    elif data2[1] == "铅笔裤":
        Pencil_pants2 += data2[4]



print("全年的销售总额为:",sum_age)
print("全年销售总件数为:",total)
print("最畅销的衣服是：T血")
print("全年销量最低的衣服是: 马甲")
print("全年羽绒服销售件数占比：",'{:.2%}'.format(down_jacket/total))
print("全年牛仔裤销售件数占比：",'{:.2%}'.format(jeans/total))
print("全年风衣销售件数占比：",'{:.2%}'.format(dust_coat/total))
print("全年皮草销售件数占比：",'{:.2%}'.format(fur/total))
print("全年T血销售件数占比：",'{:.2%}'.format(T_shirt/total))
print("全年马甲销售件数占比：",'{:.2%}'.format(vest/total))
print("全年皮衣销售件数占比：",'{:.2%}'.format(fur_clothing/total))
print("全年小西装销售件数占比：",'{:.2%}'.format(small_suits/total))
print("全年休闲裤销售件数占比：",'{:.2%}'.format(casual_pants/total))
print("全年卫衣销售件数占比：",'{:.2%}'.format(Sweater/total))
print("全年衬衫销售件数占比：",'{:.2%}'.format(shirt/total))
print("全年棉衣销售件数占比：",'{:.2%}'.format(Cotton/total))
print("全年铅笔裤销售件数占比：",'{:.2%}'.format(Pencil_pants/total))

a = "{:.2%}".format(down_jacket1/sum_age)
b = '{:.2%}'.format(jeans1/sum_age)
c = '{:.2%}'.format(dust_coat1/sum_age)
d = '{:.2%}'.format(fur1/total)
e = '{:.2%}'.format(T_shirt1/sum_age)
f = '{:.2%}'.format(vest1/sum_age)
g = '{:.2%}'.format(fur_clothing1/sum_age)
h = '{:.2%}'.format(small_suits1/sum_age)
kuzi = '{:.2%}'.format(casual_pants1/sum_age)
o = '{:.2%}'.format(Sweater1/sum_age)
p = '{:.2%}'.format(shirt1/sum_age)
q = '{:.2%}'.format(Cotton1/sum_age)
y = '{:.2%}'.format(Pencil_pants1/sum_age)
info = '''
每种衣服的全年销售额占比分别为：
                羽绒服:%s
                牛仔裤:%s
                风衣:%s
                皮草:%s
                T血:%s
                马甲:%s
                皮衣:%s
                小西装:%s
                休闲裤:%s
                卫衣:%s
                衬衫:%s
                棉衣:%s
                铅笔裤:%s
                '''
print(info % (a,b,c,d,e,f,g,h,kuzi,o,p,q,y))
print("一月份总销售量:", total1)
info = '''
每种衣服的销售额占比分别为：
                羽绒服:%s
                牛仔裤:%s
                风衣:%s
                皮草:%s
                T血:%s
                马甲:%s
                皮衣:%s
                小西装:%s
                休闲裤:%s
                卫衣:%s
                衬衫:%s
                棉衣:%s
                铅笔裤:%s
'''






















