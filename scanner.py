from tokens import *
import re

class Scanner:
    def isOperator(self,char):
        if char in operators:
            return True
        return False

    def getOperator(self,line,index):
        token=''

        while index<len(line) and self.isOperator(line[index]):
            token+=line[index]
            index+=1

        return [token,index]

    def getString(self,line,index):
        token=''
        quotes=0

        while index<len(line) and quotes<2:
            if line[index]== '"':
                quotes+=1
            token+=line[index]
            index +=1

        return [token,index]

    def tokenize(self,line,separators):
        token=''
        index=0

        while index<len(line):
            if self.isOperator(line[index]):
                if token:
                    yield token
                token=self.getOperator(line,index)[0]
                index=self.getOperator(line,index)[1]
                yield token
                token=''
            elif line[index]=='"':
                if token:
                    yield token
                token=self.getString(line,index)[0]
                index=self.getString(line,index)[1]
                yield token
                token = ''
            elif line[index] in separators:
                if token:
                    yield token
                token=line[index]
                index=index+1
                yield token
                token = ''
            else:
                token+= line[index]
                index+=1
        if token:
            yield token


    def isIdentifier(self,token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None

    def isConstant(self,token):
        #return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None
        letters = list(token)

        if letters[0] == '0' and len(letters) > 1:
            return False
        elif letters[0] in ['+', '-'] and len(letters) > 1 and letters[1] == '0':
            return False
        elif letters[0] == '*':
            return False
        else:
            return True


