"""
    @Name : Ronit kumar Patel
    @Title : Prime number
"""
import logging

log = '%(lineno)d -- %(asctime)s -- %(message)s'
logging.basicConfig(filename='prime_number.log', filemode='w', format=log, level=logging.DEBUG)


def prime_num(num):
    """
    Writing a code for prime number
    :param num:
    :return: nothing
    """
    logging.debug("Prime number code")
    try:
        for i in range(2, num):
            if num % i == 0:
                print("This is not a prime number")
                break
        else:
            print("This is a prime number")
    except Exception as e:
        print(e)
        logging.warning("This code is only calculating the prime numer")


if __name__ == "__main__":
    try:
        num = int(input("Enter the number : "))
        prime_num(num)
    except Exception as e:
        print(e)
        logging.error("This code is only calculating the prime numer")