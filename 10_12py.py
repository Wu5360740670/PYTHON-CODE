tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
tinydict['School'] = "RUNOOB"#添加
print("tinydict['School']: ", tinydict['School'])
print(tinydict)

#时间
import time
ticks=time.time()
print(ticks)

localtime=time.localtime(time.time())
print(localtime)
#asctime,格式化时间
localtime2=time.asctime(time.localtime(time.time()))
print(localtime2)


import calendar
 
cal = calendar.month(2023,10 )
print(cal)



#函数
