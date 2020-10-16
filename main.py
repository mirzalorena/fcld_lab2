# This is a sample Python script.

from symbolTable import SymbolTable

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print("Hello")

    symbolTable = SymbolTable()

    symbolTable.add(["a",7])
    symbolTable.add(["b",5])
    symbolTable.add(["c",8])
    symbolTable.add(["d",11])

    print(symbolTable.get("a"))
    print(symbolTable.get("e"))

    print(symbolTable.getPosition("a"))
    print(symbolTable.getPosition("d"))
    print(symbolTable.getPosition("g"))



