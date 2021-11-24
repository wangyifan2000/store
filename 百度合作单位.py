import xlrd
bd = xlrd.open_workbook(filename=r'D:\python\保存位置\python\任务\day09\百度合作单位-人员管理-二期.xls')
st = bd.sheet_by_index(0)
rows = st.nrows
print("百度合作单位一共有：", rows-1,"人")
man = 0
ko = 0
ok = 0
nianling = 0
pay = 0
pay1 = 0
dianxin = 0
yidong = 0
liantong = 0
Amur_River = 0
Beijing = 0
fujian = 0
sichuan = 0
chuanmei = 0
for a in range(1, rows):
    data = st.row_values(a)
    if data[8] == "男":
        ko += 1
    elif data[8] == "女":
        ok += 1
    if data[7] > 45:
        nianling += 1
    if data[11] > 8000:
        pay = pay + 1
    elif data[11] < 3000:
        pay1 += 1
    if data[5].startswith("14" or "17"):
        dianxin += 1
    elif data[5].startswith("13"):
        yidong += 1
    elif data[5].startswith("15"):
        liantong += 1
    if data[9].startswith("黑龙江"):
        Amur_River += 1
    elif data[9].startswith("北京"):
        Beijing += 1
    elif data[9].startswith("福建"):
        fujian += 1
    elif data[9].startswith("四川"):
        sichuan += 1
    if data[13].endswith("传媒有限公司"):
        chuanmei += 1


print("男生人数为：",ko)
print("女生人数为：",ok)
print("年龄超过45岁的人数为：",nianling)
print("薪资超过8000的人员数量有：",pay)
print("薪资低于3000的人员数量有：",pay1)
print("电信用户数量为：", dianxin)
print("移动用户数量为：",yidong)
print("联通用户数量为：",liantong)
print("在黑龙江地区的人数为：",Amur_River)
print("在北京地区的人数为：",Beijing)
print("在福建地区的人数为：",fujian)
print("在四川地区的人数为：",sichuan)
print("在传媒公司工作的人数为：",chuanmei)












