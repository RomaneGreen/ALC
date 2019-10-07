from util import *


def start_encode():

    while True:
        try:
            enc = int(input("Please enter a number in the range of -8192 to 8191 or enter any other key to exit "))
            if -8192 <= enc <= 8191:
                print("The of value", enc, "encoded is", encode(enc))
            else:
                continue
        except ValueError:
            break


def start_decode():

    while True:
        try:
            dnc = int(input("Please enter a hex value in between 0x0000 and 0x7F7F or enter any other key to exit "), 16)
            if 0x0000 <= dnc <= 0x7F7F:
                byte = divide_byte(dnc)
                print("The of value", hex(dnc), "decoded is", decode(byte[0], byte[1]))
        except ValueError:
            break


def start_options():

    while True:
        print("Enter e to start encode")
        print("Enter d to start decode")
        print("Enter x to terminate program")

        txt = input().lower()
        if txt == "x":
            print("Aidos")
            break
        elif txt == "e":
            start_encode()
        elif txt == "d":
            start_decode()


start_options()