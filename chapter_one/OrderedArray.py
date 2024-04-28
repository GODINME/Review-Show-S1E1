"""Implementation of Ordered Array Abstract Data Type"""

class OrderedArray(object):

    """Constructor: A method that initialized an empty ordered array with allocated fixed size"""
    def __init__(self, size):
        self.__ordered_array = [None] * size 
        self.__size = 0


    """find: A method that locate the index position on an item in ordered array using binary search algorithm"""
    def find(self, item):
        lower = 0
        upper = self.__size - 1

        while lower <= upper:
            middle = (lower + upper) // 2
            
            if self.__ordered_array[middle] == item:
                return middle
            elif self.__ordered_array[middle] > item:
                upper = middle - 1
            else:
                lower = middle + 1
        return lower 


    """get: A method that locate an item in ordered array based on its index position given"""
    def get(self, index):
        if 0 <= index and index < self.__size:
            return self.__ordered_array[index]
        raise IndexError("Index " + str(index) + " out of range")


    """show: A method that traverse through all the item in the ordered array"""
    def show(self, display=print):
        for index in range(self.__size):
            display(self.__ordered_array[index])



    """len: A function that return the number of items in the ordered array"""
    def __len__(self):
        return self.__size 


    """str: A function that gives a string representation of our ordered array automatically"""
    def __str__(self):
        output = "["
        for index in range(self.__size):
            if len(output) > 1:
                output += ", "
            output += str(self.__ordered_array[index])
        output += "]"
        return output 


    """search: A method that return the search item if it exit in the ordered array"""
    def search(self, item):
        index = self.find(item)
        if index < self.__size and self.__ordered_array[index] == item:
            return self.__ordered_array[index]


    """insert: A method that insert an item into the ordered array in an ordering manner"""
    def insert(self, item):
        if self.__size >= len(self.__ordered_array):
            raise Exception("Array Overflow")

        index = self.find(item)

        for shift_index in range(self.__size, index, -1):
            self.__ordered_array[shift_index] = self.__ordered_array[shift_index-1]
        self.__ordered_array[index] = item
        self.__size += 1


    """delete: A method that remove an item in the ordered array"""
    def delete(self, item):
        index = self.find(item)
        if index < self.__size and self.__ordered_array[index] == item:
            self.__size -= 1
            for shift_index in range(index, self.__size):
                self.__ordered_array[shift_index] = self.__ordered_array[shift_index+1]
            return True
        return False


    """capacity: A method that return the number of items the ordered array can hold"""
    def capacity(self):
        return len(self.__ordered_array)
