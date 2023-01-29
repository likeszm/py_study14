#py学习记录14：时间
"""



"""
import time
import datetime


#1.获取当前时间(秒数格式)
"""
print( time.time() )
"""


#2.获取当前时间(字符串格式)
"""
#标准格式
print(datetime.datetime.now() )
#自定义格式
print(datetime.datetime.now().strftime('%Y年%m月%d日 -- %H : %M : %S') )
#或者：
print(  time.strftime('%Y年%m月%d日 -- %H : %M : %S', time.localtime()) )
#还可以自定义时间秒数
print(  time.strftime('%Y年%m月%d日 -- %H : %M : %S', time.localtime(1434502529)) )
#反向转换
Mytime = int(time.mktime(time.strptime('2015-08-01 23:59:59', '%Y-%m-%d %H:%M:%S')))
print(Mytime)
"""


#3.获取日期特定的数据
"""
str_time = datetime.datetime.now().year
str_time = datetime.datetime.now().month
str_time = datetime.datetime.now().day
str_time = datetime.datetime.now().hour
str_time = datetime.datetime.now().minute
str_time = datetime.datetime.now().second

print(str_time)
"""


#4.查询是周几
"""
thatDay = "2023-1-29"
theDay = datetime.datetime.strptime(thatDay,'%Y-%m-%d')
print(theDay.weekday())
"""


