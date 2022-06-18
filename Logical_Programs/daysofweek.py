"""
    @Name : Ronit kumar Patel
    @Title : days of weeks
"""
import logging
from datetime import date

log = '%(lineno)d--%(asctime)s--%(message)s'
logging.basicConfig(filename="vending_machine.log", format=log, filemode='w', level=logging.DEBUG)


def day_of_week(year, month, day):
    logging.debug("Days of week program will running ......")
    mm = 0
    mm = date.year, date.month, date.day
    print(mm)
    y = year - (14 - mm) / 12
    x = y + y / 4 - y / 100 + y / 400
    m = mm + 12 * ((14 - mm) / 12) - 2
    d = (day + x + (31 * m) / 12) % 7



if __name__ == "__main__":
    year = int(input("Input a year: "))
    month = int(input("Input a month [1-12]: "))
    day = int(input("Input a day [1-31]: "))

    day_of_week(year, month, day)
