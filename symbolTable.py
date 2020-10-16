from bst import BST

class SymbolTable:
    def __init__(self):
        self.__bst=BST()

    def add(self,value):
        return self.__bst.insert(value)

    def get(self,value):
        return self.__bst.find(value)

    def __str__(self):
        return str(self.__bst)
