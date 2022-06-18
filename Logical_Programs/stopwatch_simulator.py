"""
    @Name : Ronit kumar Patel
    @Title : Stopwatch simulator
"""
import logging
from time import time

log = '%(lineno)d--%(asctime)s--%(message)s'
logging.basicConfig(filename="stopwatch.log", format=log, filemode='w', level=logging.DEBUG)


def stopwatch(num):
    """
    Writing a code for stopwatch simulator
    :param num:
    :return: nothing
    """
    logging.debug("Stopwatch simulator running perfactly")
    print("Stopwatch running..")
    t = time()
    watch = 0
    try:
        while watch - t < num:
            watch = time()

        print(" Finished!\n Time =", watch - t)
    except Exception as e:
        print(e)
        logging.exception("There is something occurs please re-check the code")


if __name__ == "__main__":
    try:
        num = int(input("Enter the number : "))
        stopwatch(num)
    except Exception as e:
        print(e)
        logging.warning("Warning !!")
    else:
        print("Stop")
    finally:
        print("Finally Executed")

