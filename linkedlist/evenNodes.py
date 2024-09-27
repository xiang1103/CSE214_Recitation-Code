import LinkedList

#recitation 2, Even nodes Check 
def hasEvenNodes(list): 
    cur= list.head 
    if cur is None: 
        return False 
    while cur is not None: 
        if cur.next is None: 
            return False 
        else: 
            cur = cur.next.next 
    return True 


def main(): 
    list= LinkedList.LinkedList() 
    list.addFirst(1)
    list.addLast(3) 
    list.addLast(4) 
    list.addLast(5) 
    list.print() 
    print(hasEvenNodes(list))


if __name__ == "__main__":
    main() 