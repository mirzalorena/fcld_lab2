class ProgramInternalForm:
    def __init__(self):
        self.__list=[]

    def add(self,content,id):
        self.__list.append((content,id))

    def __str__(self):
        return str(self.__list)