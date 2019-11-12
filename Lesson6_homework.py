import pandas as pd
import csv

dataset = \
"""色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""

id_coloumn = ['编号']
lines_no = list(range(len(dataset.split('\n'))-1))
lines_no = list(map(lambda x: x+1, lines_no))
id_coloumn = id_coloumn + lines_no


lines = dataset.split('\n')
file = 'machine_learning.csv'
with open(file, 'w', encoding = 'utf-8') as f:
    for id_no, line in zip(id_coloumn, lines):
        f.write(str(id_no) + ' ' + line + '\n')
print('csv file is generated!')

data_add = \
"""青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 好"""
with open(file, 'a', encoding = 'utf-8') as f:
    f.write(str(len(dataset.split('\n'))) + ' ' + data_add)

df = pd.read_csv(file) # pandas 验证
print(df.head())

columns = []
datalist = []

with open(file, 'r', encoding = 'utf-8') as f:
    first_line = f.readline().split("\n")[0]
    columns = first_line.split(' ')
    lines = f.readlines()

datalist = [line.split("\n")[0].split(' ')[1:] for line in lines]

# validate
print(columns==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1]==['青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '好'])

# 在所有数据中过滤出色泽='浅白'的数据
filter_white = lambda data: data[0] == '浅白'
data_filter_white = list(filter(filter_white, datalist))
# 在所有数据中过滤出密度大于0.5的数据
filter_density = lambda data: float(data[6]) > 0.5
data_filter_density = list(filter(filter_density, datalist))
