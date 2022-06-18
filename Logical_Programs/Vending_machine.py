"""
    @Name : Ronit kumar Patel
    @Title : Vending Machine
"""
import logging

log = '%(lineno)d--%(asctime)s--%(message)s'
logging.basicConfig(filename="vending_machine.log", format=log, filemode='w', level=logging.DEBUG)


def vending_machine(change):
    """
    Writing a code for vending machine
    this program is like little atm machine
    :return: nothing
    """
    logging.debug("Vending machine perfectly running.............")
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    j = 0
    rupees = change
    notesfrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    is_start = True
    try:
        while True:
            for i in range(len(notes)):
                if rupees > notes[i] or rupees == notes[i] and (not is_start):
                    j = i
                    break
            rupees = rupees - notes[j]
            notesfrequency[j] += 1
            if rupees == 0:
                break
            is_start = False
        for i in range(len(notesfrequency)):
            if notesfrequency[i] > 0:
                print(f"frequency of {notes[i]} rupees note : {notesfrequency[i]}")
    except Exception as e:
        print(e)
        logging("There is something occurs please re-check the code")


if __name__ == "__main__":
    try:
        change = int(input("Enter the amount : "))
        vending_machine(change)
    except Exception as e:
        print(e)
        logging.warning("Warning !!")
    else:
        print("Successfully withdraw your amount")
    finally:
        print("Take your change !")
