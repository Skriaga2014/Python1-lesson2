import random
import datetime

#date = "{}.{}.{}".format(random.randrange(1,30), random.randrange(1,12), random.randrange(1980,2018))

date = datetime.date(random.randrange(1980,2018),random.randrange(1,12),random.randrange(1,30))
date = (date.strftime("%d.%m.%Y"))

print("Дата:", date)

day_int = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
day_str = ["Первое","Второе","Третье","Четвертое","Пятое","Шестое","Седьмое","Восьмое","Девятое","Десятое",
           "Одиннадцатое","Двенадцатое","Тринадцатое","Четырнадцатое","Пятнадцатое","Шестнадцатое","Семьнадцатое",
           "Восемьнадцатое","Девятнадцатое","Двадцатое","Двадцать первое","Двадцать второе","Двадцать третье",
           "Двадцать четвертое","Двадцать пятое","Двадцать шестое","Двадцать седьмое","Двадцать восьмое",
           "Двадцать девятое","Тридцатое"]

mon_int = ["01","02","03","04","05","06","07","08","09","10","11","12",]
mon_str = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]



day = day_str[day_int.index(date[0:2])]
# ИЛИ: day = day_str[int(date[0:2])-1]
mon = mon_str[mon_int.index(date[3:5])]
yr = date[6:10]

print (day, mon, yr, "года")

print("\n\nГОТОВО!")