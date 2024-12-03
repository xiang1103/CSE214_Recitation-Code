from tree import * 

def main():
    root= Tree(5) 
    insert (root, 40)
    insert (root, 30)
    insert (root, 25)
    insert (root, 35)
    insert (root, 50)
    insert (root, 45)
    insert (root, 60)
    preorder_trav(root)

if __name__ == "__main__":
    main() 
    