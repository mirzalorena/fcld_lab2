from symbolTable import SymbolTable
from token import *
from scanner import *

if __name__ == '__main__':
    '''
    print("Hello")

    symbolTable = SymbolTable()
    
    symbolTable.add(["a", 7])
    symbolTable.add(["b", 5])
    symbolTable.add(["c", 8])
    symbolTable.add(["d", 11])

    print(symbolTable.get("a"))
    print(symbolTable.get("e"))

    print(symbolTable.getPosition("a"))
    print(symbolTable.getPosition("d"))
    print(symbolTable.getPosition("g"))
    '''

    scanner=Scanner()

    filename=input("Choose file: ")
    fopen=open(filename,'r')
    print("Code: ")
    for line in fopen:
        print(line)

    print("Tokenized: ")
    with open(filename,'r') as fopen:
        for line in fopen:
            print([token for token in scanner.tokenize(line,separators)])










