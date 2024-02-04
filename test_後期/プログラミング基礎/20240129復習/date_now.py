import datetime

now = datetime.datetime.now()
print(now.date())
print(now.time())
now_f = datetime.datetime.strftime(now,'%Y年%m月%d日')
print(now_f)

weekday = list('月火水木金土日')

now_weekday = datetime.date.weekday(now)
print(weekday)
print(f'今日は、{weekday[now_weekday]}曜日')