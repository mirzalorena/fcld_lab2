separators = ['[', ']', '{', '}', '(', ')', ';', ' ', '\n']
operators = ['+', '-', 'X*', '/', '%', '<', '<=', '=', '>=', '>',
             '&', '||', '!=',  ',', '<-']
reservedWords=['input','prettyPrint','Int','Float',
               'Char','onlyIf','soElse','justFor','Void','While','Do']
everything = separators + operators + reservedWords

codification=dict()
codification['id']=0
codification['const']=1
for i in range(len(everything)):
    codification[everything[i]]=i+2
