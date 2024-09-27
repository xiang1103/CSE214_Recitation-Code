#Given a linked list, swap every two nodes 


def swapPairs(self, head): 
    dummy = Node(0)
    dummy.next= head
    cur= head  
    prev= dummy 
    while (cur is not None and cur.next is not None):
        nextPair= cur.next.next 
        secondNode= cur.next 
        secondNode.next= cur 
        cur.next= nextPair 
        prev.next= secondNode 
        prev= cur 
        cur= nextPair 
    return dummy.next 