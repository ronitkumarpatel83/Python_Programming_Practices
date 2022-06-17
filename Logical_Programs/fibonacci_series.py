"""
    @Name : Ronit kumar Patel
    @Title : Fibonacci Series
"""
import logging

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='fibo.log', filemode='w', format=log, level=logging.DEBUG)


def fib(n):
    """
    Writing here a program for fibonacci series
    using try except exception and logging
    :param n:
    :return: nothing
    """
    logging.debug("Fibonacci series")
    a, b = 0, 1
    try:
        while a < n:
            a, b = b, a + b
            print(a, end=' ')
    except Exception as e:
        print(e)
        logging.warning("This code is only calculating the fibonacci numer")


if __name__ == "__main__":
    n = int(input("Enter the number : "))
    fib(n)
    logging.error("This code is only calculating the fibonacci numer")
