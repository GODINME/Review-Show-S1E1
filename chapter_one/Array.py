"""Implementation of an Array Data Type"""

class Array(object):

    """A constructor that initialize an empty array with a fxed size memory allocation"""
    def __init__(self, size):
        self.__array = [None] * size 
        self.__size = 0 


    """len: A function that return the number of items in the array"""
    def __len__(self):
        return self.__size 


    """get: A method that return the value or item at a given index"""
    def get(self, index):
        if 0 <= index and index < self.__size:
            return self.__array[index]


    """set: A method that override item or value in the array base on its index"""
    def set(self, index, item):
        if 0 <= index and index < self.__size:
            self.__array[index] = item


    """insert: A method that add item at end of the array"""
    def insert(self, item):
        self.__array[self.__size] = item
        self.__size += 1


    """find: A method that locate the index position of an item in array"""
    def find(self, item):
        for index in range(self.__size):
            if self.__array[index] == item:
                return index
        return -1


    """search: A method that locate an item in array"""
    def search(self, item):
        return self.get(self.find(item))


    """remove: A method that delete item in the array"""
    def remove(self, item):
        for index in range(self.__size):
            if self.__array[index] == item:
                self.__size -= 1
                for delkey in range(index, self.__size):
                    self.__array[delkey] = self.__array[delkey+1]
                return True
        return False


    """show: A method that traverse and display all items in the array"""
    def show(self):
        for index in range(self.__size):
            print(self.__array[index], "at index", index)
