#!/usr/bin/python3
"""Module that contains a function that writes a string
to a text file (UTF8)"""


def append_write(filename="", text=""):
    """Function that writes a string to a text file (UTF8) and
    returns the number of characters written. Appends the text
    to the contents of the file.

    Args:
        filename (str): name of file to write to
        text (str): text to add to the contents of the file.

    """

    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)

if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt",
                                       "Holberton School is so cool!\n")
    print(nb_characters_added)
