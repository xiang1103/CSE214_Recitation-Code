#implement binary search tree and basic functions 

class Tree():
    def __init__ (self, val):
        self.val = val 
        self.left= None 
        self.right= None 

def insert(root, key):
    if root is None: 
        root= Tree(key) 
        return root 
    if root.val==key:
        return root 
    elif key<root.val: 
        root.left= insert(root.left, key)
    else: 
        root.right= insert(root.right,key)
def preorder_trav(root):
    if (root!=None):
        print(root.val, end="->")
        preorder_trav(root.left)
        preorder_trav(root.right)
    else:
        return root 
def inorder (root):
    if root is not None: 
        inorder(root.left)
        print(root.val, end="->")
        inorder(root.right)
    else:
        return root 
def postorder(root):
    if root is not None: 
        postorder(root.left)
        postorder(root.right)
        print(root.val, end="->")
    else: 
        return root 

def main(): 
    root= Tree(5)
    insert(root, 2)
    #root.insert(7)
    #root.inorder() 
    #print(root.val)

if __name__ == "__main__":
    main() 

            