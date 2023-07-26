#!/usr/bin/python3
""" module contaiing the class MyList that is a subclass of list"""


class MyList(list):
    """Contains an extra method to print an accending sort version of the list.
    Assumes the list is make up of ints. """

    def print_sorted(self):
        """ prints a sorted version of the MyList """
        new_list = self.copy()
        new_list.sort()
        print(new_list)

if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
