# coding:utf-8

from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(type(now), now)


three_days = timedelta(days=3)
after_three_days = now + three_days
print(after_three_days)
before_three_days = now - three_days
print(before_three_days)

one_hour = timedelta(hours=1)
before_one_hour = now - one_hour
print(before_one_hour)

# 时间对象无法传输,通过函数strftime 转成字符串格式
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print('now_str==>', now_str, type(now_str))
after_three_days_str = after_three_days.strftime('%Y/%m/%d %H:%M:%S')
print(after_three_days_str, type(after_three_days_str))
before_one_hour_str = before_one_hour.strftime('%H:%M:%S')
print(before_one_hour_str)


# 字符串时间转时间对象, 后面的格工需要和字符串的格式保持一致
now_obj = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
print('now_obj==>', now_obj, type(now_obj))
after_three_days_obj = datetime.strptime(after_three_days_str, '%Y/%m/%d %H:%M:%S')
print(after_three_days_obj, type(after_three_days_obj))
before_one_hour_obj = datetime.strptime(before_one_hour_str, '%H:%M:%S')
print(before_one_hour_obj, type(before_one_hour_obj))

# datetime 生成时间戳
shijiancuo = datetime.timestamp(datetime.now())
print(shijiancuo)

# 时间戳转对象，返回日期对象
shijiancuo_obj = datetime.fromtimestamp(shijiancuo)
print(shijiancuo_obj, type(shijiancuo_obj))