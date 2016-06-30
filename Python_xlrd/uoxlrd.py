#coding=utf-8

import xlrd

#打开一个Excel文件
data=xlrd.open_workbook('myExcel.xlsx')

#获取一个工作表
#table=data.sheets()[0]
#table=data.sheet_by_index(1)#通过索引顺序获取
#table=data.sheet_by_name(u'测试用例')
t=data.sheets()
print t
table=t[0]
#获取一整列的值
n=0

'''
while table.row_values(n):

    n+=1
    '''


#print table.col_values(0)
nrow=table.nrows#读取Excel表格的行数
ncol=table.ncols#读取表格的列数
print nrow,ncol
testcase=[] #筛选出要进行测试的用例
for i in range(nrow):
    if table.cell(i,1).value == u'是':
        testcase.append(table.cell(i,0).value)


#print testcase
      
#print table.row_values(0) #打印第一行
#print table.col_values(0) #打印第一列

#print table.row(0)[1].value #打印第一行，第2列
print table.col(0)[1].value
#print table.cell(0,1).value #打印指定单元格的值

row=0
col=0
ctype=1
value=u'单元格的值'
xf=0 #扩展的格式化
table.put_cell(row,col,ctype,value,xf)

print table.cell(0,0).value 

