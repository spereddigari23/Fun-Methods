class Node:
    def __init__(self,data):
        this.data=data;
        this.left=None
        this.right=None
def traverseInOrder(rootnode):
    t=rootnode
    while t!=None:
        traverseInOrder(t.left)
        print(t.data)
        traverseInOrder(t.right)
def preOrderTraversal(rootnode):
    t=rootnode
    while t!=None:
        print(t.data)
        preOrderTraversal(t.left)
        preOrderTraversal(t.right)
    
def postOrderTraversal(rootnode):
    t=rootnode
    while t!=None:
        postOrderTraversal(t.left)
        postOrderTraversal(t.right)
        print(t.data)