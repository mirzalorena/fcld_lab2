from symbolTable import SymbolTable
from token import *
from scanner import *
from programInternalForm import ProgramInternalForm

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

    print("\nTOKENIZED: ")
    with open(filename,'r') as fopen:
        for line in fopen:
            print([token for token in scanner.tokenize(line,separators)])

    symbolTable=SymbolTable()
    pif=ProgramInternalForm()

    with open(filename,'r') as fopen:
        flag=0
        count=0
        for line in fopen:
            count+=1
            for token in scanner.tokenize(line[0:-1],separators):
                if token in everything:
                    ''''''
                if scanner.isIdentifier(token):
                    symbolTable.add(token)
                elif scanner.isConstant(token):
                    symbolTable.add(token)
                else:
                    flag=1
                    #raise Exception("Token not found "+token+" at line "+str(count))

    if(flag==0):
        print("Lexically correct")
    else:
        print("Lexically incorrect")

    print("Program Internal Form: \n" + pif.__str__())
    print("Symbol Table: \n"+symbolTable.__str__())











