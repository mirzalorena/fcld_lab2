# This is a sample Python script.

from symbolTable import SymbolTable

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    print("Hello")

    symbolTable = SymbolTable()

    symbolTable.add("a")
    symbolTable.add("b")
    symbolTable.add("c")
    symbolTable.add("d")

    print(symbolTable.getPosition("d"))



