from datetime import date

mm = date.year(), date.month(), date.day()
print(mm)
y = year - (14 - mm) / 12
x = y + y / 4 - y / 100 + y / 400
m = mm + 12 * ((14 - mm) / 12) - 2
d = (day + x + (31 * m) / 12) % 7
