#!/usr/bin/python3
"""Module that contains a function that writes a string
to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8) and
    returns the number of characters written. Overwrites the contents
    of the file.

    Args:
        filename (str): name of file to write to
        text (str): text to set the contents of the file to.

    """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return len(text)

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt",
                               "Holberton School is so cool!\n")
    print(nb_characters)
