class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.value

    def getElem(self):
        return self.value[0]

    def set(self, val):
        self.value = val

    def setRight(self, right):
        self.rightChild = right

    def setLeft(self, left):
        self.leftChild = left

    def getChildren(self):
        children = []
        if (self.leftChild != None):
            children.append(self.leftChild)
        if (self.rightChild != None):
            children.append(self.rightChild)
        return children

    def insert(self, d):
        if self.value[0] == d[0]:
            return False
        elif d[0] < self.value[0]:
            if self.leftChild:
                return self.leftChild.insert(d)
            else:
                self.leftChild = Node(d)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(d)
            else:
                self.rightChild = Node(d)
                return True


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, value):
        self.root = Node(value)

    def getRoot(self):
        return self.root

    def add(self,value):
        if self.root:
            print("ROOT: "+self.root.value[0])
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True


    def insert(self, value):
        if (self.root is None):
            self.setRoot(value)
            print("ROOT: " +self.getRoot().value[0])
            return self.root
        else:
            rootAux=Node(self.root.value)
            return self.insertNode(rootAux, value)

    def insertNode(self, currentNode, value):
        if(value[0]==currentNode.value[0]):
            currentNode.value=value
        elif (value[0] < currentNode.value[0]):
            if (currentNode.leftChild):
                print("LEFT: "+currentNode.leftChild.value[0])
                self.insertNode(currentNode.leftChild, value)
            else:
                currentNode.leftChild = Node(value)
        elif (value[0] > currentNode.value[0]):
            if (currentNode.rightChild):
                print("RIGHT: " + currentNode.rightChild.value[0])
                self.insertNode(currentNode.rightChild, value)
            else:
                currentNode.rightChild = Node(value)
        return currentNode

    def find(self, value):
        return self.findNode(self.root, value)

    def findNode(self, currentNode, value):
        if (currentNode is None):
            return False
        elif (value[0] == currentNode.value[0]):
            return True
        elif (value[0] < currentNode.value[0]):
            return self.findNode(currentNode.leftChild, value)
        else:
            return self.findNode(currentNode.rightChild, value)


    def findPosition(self, value):
        if self.find(value) is False:
            return -1

        position = 0
        if self.root is None or self.root.value == value:
            return position

        while self.root != None:
            if value[0] > self.root.value[0]:
                position += 1
                self.root = self.root.rightChild
            elif value[0] < self.root.value[0]:
                position += 1
                self.root = self.root.leftChild
            else:
                return position

        return position

    def in_order(self):
        if self.root is not None:
            return self.aux(self.root)

    def aux(self, root):
        if root is None:
            return ''

        if root is not None:
            left = self.aux(root.leftChild)
            right = self.aux(root.rightChild)
            return left + ' ' + str(root.value) + ' ' + right

    def inorder(self, root):
        if root:
            self.inorder(root.leftChild)
            print(root.value)
            self.inorder(root.rightChild)
