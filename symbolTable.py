from bst import BST

class SymbolTable:
    def __init__(self):
        self.__bst=BST()

    def add(self,value):
        return self.__bst.add(value)

    def get(self,value):
        return self.__bst.find(value)

    def getRoot(self):
        return self.__bst.getRoot()

    def setRoot(self,root):
        return self.__bst.setRoot(root)

    def getPosition(self,value):
        return self.__bst.findPosition(value)

    def getIndex(self,value):
        return self.__bst.findIndex(value)

    def __str__(self):
        return self.__bst.in_order()


