from LinkedList import * 

#find the second to last node 
def find(list):
    head= list.head 
    if head is None or head.next is None: 
        return None 
    while head.next.next is not None: 
        head = head.next 
    return head.val 
    


def main(): 
    list= LinkedList() 
    list.addFirst(1)
    list.addLast(3) 
    list.addLast(4) 
    list.addLast(5) 
    list.addLast(0)
    list.addLast(0)
    list.addLast(1)
    list.addLast(5)
    print(find(list)) 


if __name__ == "__main__":
    main() 