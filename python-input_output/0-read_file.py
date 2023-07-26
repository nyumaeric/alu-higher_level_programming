#!/usr/bin/python3
"""Module containing a function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, mode="r") as file:
        print(file.read(), end="")

if __name__ == "__main__":
    read_file("my_file_0.txt")
