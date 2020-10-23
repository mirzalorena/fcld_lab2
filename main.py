# This is a sample Python script.

from symbolTable import SymbolTable

if __name__ == '__main__':

    print("Hello")

    symbolTable = SymbolTable()

    symbolTable.add("a")
    symbolTable.add("b")
    symbolTable.add("c")
    symbolTable.add("d")

    print(symbolTable.get("a"))
    print(symbolTable.get("e"))

    print(symbolTable.getPosition("a"))
    print(symbolTable.getPosition("d"))
    print(symbolTable.getPosition("g"))





