import tushare as ts

df = ts.get_hist_data('000001')
# 直接保存
# 修改列名 第一列修改不了？
# df.columns = ['日期','日期', '开盘价', '最高价', '闭市价', '最低价', '开盘价', '最高价', '闭市价', '最低价', '开盘价', '最高价', '闭市价']
df.to_csv('000001.csv')
df.to_excel('000001.xls')
# #设定数据位置（从第3行，第6列开始插入数据）
# df.to_excel('0001.xlsx', startrow=2,startcol=5)
# df.to_csv('000001.csv')
