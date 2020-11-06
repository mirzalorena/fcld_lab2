class FiniteAutomata:
    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F

    def isState(self,value):
        return value in self.Q

    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    def getTransactions(trans):
        result = []
        transitions = []
        index = 0

        while index < len(trans):
            transitions.append(trans[index] + ',' + trans[index + 1])
            index += 2

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
            S = FiniteAutomata.getTransactions(FiniteAutomata.parseLine(''.join([line for line in file])))

            return FiniteAutomata(Q, E, S, q0, F)

    def __str__(self):
        return 'Q =' + str(self.Q) + ' \n' \
               + 'E =  ' + str(self.E)+ ' \n' \
               + 'F = ' + str(self.F) + ' \n' \
               + 'q0 = ' + str(self.q0) + '\n'\
               + 'S = { ' + '\n '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n'


if __name__ == '__main__':
    print("Test Finite Automata")

    fa=FiniteAutomata.fromFile("fa.txt")
    print(fa)


