# -*- coding: utf-8 -*

# ------准备-------
header = ['平均']
data = []
output_list = []
l2_list = []

# ------打开文件------
with open('report.txt', 'r', encoding='utf-8') as f:
    for l in f.readlines():
        a = l.split()
        data.append(a)

# ------计算总分-------
l1 = len(data)
l2 = len(data[0])
for number in range(1, l1):
    d1 = data[number]
    total_scores = 0
    for scores in range(1, l2):
        total_scores += float(d1[scores])
    # ------计算平均分--------
    if l2 > 1:
        ave_scores = total_scores / (l2-1)
    else:
        ave_scores = 0
    # ------存储---------
    d1.append(str(total_scores))
    d1.append(str(round(ave_scores, 1)))

# ------排序---------
data.sort(key=lambda x: x[-1], reverse=True)

# -----添加排名------
for number in range(0, l1):
    data[number].insert(0, str(number))

# ------汇总每课平均分--------
ave = 0
for width in range(2, l2+3):
    ave_all = 0
    for length in range(1, l1):
        ave_all += float(data[length][width])
        if float(data[length][width]) < 60:
            data[length][width] = '不及格'
        if l1 > 1:
            ave = ave_all/(l1-1)
        else:
            ave = 0
    header.append(str(round(ave, 1)))
header.insert(0, '0')
data.insert(1, header)

# -----添加标题行-------
data[0][0] = '名次'
data[0].append('总分')
data[0].append('平均分')

# ------输出到文件-------
for i in data:
    j = '\t'.join(i) + '\n'
    output_list.append(j)
with open('report_out.txt', 'w', encoding='utf-8') as f:
    f.writelines(output_list)
