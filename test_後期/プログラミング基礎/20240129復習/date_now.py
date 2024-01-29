import datetime

now = datetime.datetime.now()
print(now.date())
now_f = datetime.datetime.strftime(now,'%Y年%m月%d日')
print(now_f)