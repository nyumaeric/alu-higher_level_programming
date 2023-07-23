#!/usr/bin/python3)
class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage:
if __name__ == "__main__":
    # Create an instance of MyList
    my_list = MyList([5, 2, 8, 1, 3])

    # Call the print_sorted method
    my_list.print_sorted()
