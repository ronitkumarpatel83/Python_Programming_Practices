"""
    @Name : Ronit kumar Patel
    @Title : Coupon number
"""
import logging
import random
import string

log = '%(lineno)d--%(asctime)s--%(message)s'
logging.basicConfig(filename="Coupon_Number.log", format=log, filemode='w', level=logging.DEBUG)


def coupon_num(num):
    """
    writing a code for coupon number
    :param num:
    :return: number
    """
    logging.debug("Coupon Number is running perfactly...")
   # rand = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand = string.digits+string.ascii_lowercase+string.ascii_uppercase
    number = ''
    try:
        for i in range(0, num):
            start = random.randint(0, len(rand) - 1)
            number += rand[start: start + 1]
        print("This is the coupon number :- ", number)
        # return number
    except Exception as e:
        print(e)
        logging.exception("There is something occurs please re-check the code")


if __name__ == "__main__":
    try:
        num = int(input("Enter the range of coupon : "))
        coupon_num(num)
    except Exception as e:
        print(e)
        logging.warning("Warning !!")
    else:
        print("Above the coupon number claim it ! ")
    finally:
        print("Enjoy")
