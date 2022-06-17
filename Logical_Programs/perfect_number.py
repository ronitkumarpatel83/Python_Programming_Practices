"""
    @Name : Ronit kumar Patel
    @Title : Perfect Number
"""
import logging

log = '%(lineno)d -- %(asctime)s -- %(message)s'
logging.basicConfig(filename='perfect_num.log', filemode='w', format=log, level=logging.DEBUG)


def perfect_number(num):
    """
    Writing here a program for perfect number using try except exception
    :param num:
    :return:
    """
    logging.info("Perfect number")
    result = 0
    try:
        for i in range(1, num):
            if num % i == 0:
                result = result + i
        if result == num:
            print("This is a perfect number")
        else:
            print("This is not a perfect number")
    except Exception as e:
        print(e)
        logging.warning("This code id calculating perfect number only")


if __name__ == "__main__":
    try:
        num = int(input("Enter the number: "))
        perfect_number(num)
    except Exception as e:
        print(e)
        logging.error("This code id calculating perfect number only")
