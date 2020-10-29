from symbolTable import SymbolTable
from tokens import *
from scanner import *
from programInternalForm import ProgramInternalForm
from bst import *

if __name__ == '__main__':
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
                    pif.add(codification[token],-1)
                elif scanner.isIdentifier(token):
                    #print("ID: "+token)
                    symbolTable.add([token, codification['id']])

                    id=symbolTable.getPosition(token)
                    pif.add(codification['id'],id)
                elif scanner.isConstant(token):
                    #print("CONST: "+token)
                    symbolTable.add([token, codification['const']])

                    id = symbolTable.getPosition(token)
                    pif.add(codification['const'], id)
                else:
                    raise Exception("Token not found "+token+" at line "+str(count))


    print("\nProgram Internal Form: \n" + pif.__str__())
    print("Symbol Table: \n"+symbolTable.__str__())












