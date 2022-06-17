"""
    @Name : Ronit kumar Patel
    @Title : Reverse number
"""
import logging

log = '%(lineno)d -- %(asctime)s -- %(message)s'
logging.basicConfig(filename='reverse_num.log', filemode='w', format=log, level=logging.DEBUG)


def reverse_num(string):
    """
    Writing a code for reverse number
    :param string:
    :param num:
    :return: nothing
    """
    logging.debug("Reverse number code")
    try:
        reverse_string = " "
        for i in string:
            reverse_string = i + reverse_string
        print("Reversed number is : ",reverse_string)

    except Exception as e:
        print(e)
        logging.warning("This code is only calculating the reverse number")


if __name__ == "__main__":
    try:
        string = input("Enter the number : ")
        reverse_num(string)
    except Exception as e:
        print(e)
        logging.error("This code is only calculating the reverse numer")