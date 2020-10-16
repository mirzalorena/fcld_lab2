class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.value

    def set(self, val):
        self.value = val

    def getChildren(self):
        children = []
        if (self.leftChild != None):
            children.append(self.leftChild)
        if (self.rightChild != None):
            children.append(self.rightChild)
        return children

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, value):
        self.root = Node(value)

    def insert(self, value):
        if(self.root is None):
            self.setRoot(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, currentNode, value):
        if(value <= currentNode.value):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, value)
            else:
                currentNode.leftChild = Node(value)
        elif(value > currentNode.value):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, value)
            else:
                currentNode.rightChild = Node(value)

    def find(self, value):
        return self.findNode(self.root, value)

    def findNode(self, currentNode, value):
        if(currentNode is None):
            return False
        elif(value == currentNode.val):
            return True
        elif(value < currentNode.val):
            return self.findNode(currentNode.leftChild, value)
        else:
            return self.findNode(currentNode.rightChild, value)

    def findPosition(self,root,value):
        position = 0

        if root is None or root.value == value:
            return position

        while root != None:
            if value > root.value:
                position+=1
                root=root.rightChild
            elif value < root.value:
                position += 1
                root=root.leftChild
            else:
                return position

        return position
        