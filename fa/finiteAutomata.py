from scanner import *

class FiniteAutomata:
    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F

    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    def getTransitions(trans):
        result = []
        transitions = []
        count = 0

        while count < len(trans):
            transitions.append(trans[count] + ',' + trans[count + 1])
            count += 2

        for transition in transitions:
            left, right = transition.split('->')
            state2 = right.strip()
            state1, route = [value.strip() for value in left.strip()[1:-1].split(',')]

            result.append(((state1, route), state2))

        return result

    def fromFile(fileName):
        with open(fileName) as file:
            Q = FiniteAutomata.parseLine(file.readline())
            E = FiniteAutomata.parseLine(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = FiniteAutomata.parseLine(file.readline())
            S = FiniteAutomata.getTransitions(FiniteAutomata.parseLine(''.join([line for line in file])))

            return FiniteAutomata(Q, E, S, q0, F)

    def printS(self):
        return 'S = { ' + '\n '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n'

    def getSKeys(self):
        list=[]
        for i in self.S:
            list.append(i[0])
        return list

    def getSByKey(self,key):
        list=[]
        for i in self.S:
            if i[0]==key:
                list.append(i)
        return list

    def __str__(self):
        return 'Q =' + str(self.Q) + ' \n' \
               + 'E =  ' + str(self.E)+ ' \n' \
               + 'F = ' + str(self.F) + ' \n' \
               + 'q0 = ' + str(self.q0) + '\n'\
               + 'S = { ' + '\n '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n'

    def checkDFA(self):
        for i in self.getSKeys():
            if len(self.getSByKey(i))>1:
                return False
        return True

    def isAccepted(self,w,state):
        sequence=list(w)
        result=False

        for lhs in self.getSKeys():
            if lhs[0]==state and lhs[1]==sequence[0]:
                if len(sequence)==1:
                    for transition in self.getSByKey(lhs):
                        if transition[1] in self.F:
                            return True
                    return False
                else:
                    for t in self.getSByKey(lhs):
                        result=self.isAccepted(w[1:],self.getSByKey(lhs)[0][0][0])
                        if result:
                            break

        return result

    def sequenceAccepted(self,W):
        if self.checkDFA():
            return self.isAccepted(W,self.q0)

def menu():
    print("0. Exit")
    print("1. Set of states")
    print("2. The alphabet")
    print("3. Initial state")
    print("4. Final States")
    print("5. Transitions")
    print("6. FA")

if __name__ == '__main__':
    print("Test Finite Automata")
    menu()

    scanner = Scanner()
    option=-1

    fa = FiniteAutomata.fromFile("fa.txt")
    #print(fa.isAccepted('0100',fa.q0))

    while(option!=0):
        option=int(input("What do you wanna see?"))
        if(option==6):
            print(fa)
        elif option==1:
            print(fa.Q)
        elif option==2:
            print(fa.E)
        elif option==3:
            print(fa.q0)
        elif option==4:
            print(fa.F)
        elif option==5:
            print(fa.printS())







