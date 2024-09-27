import LinkedList 


#prefix: if every node of the second list is in the first list from the beginning 

#Recitation 2 LinkedList Problem
def prefix(list1, list2):
    head1= list1.head 
    head2= list2.head 
    while head2!= None:
        if head2.val != head1.val: 
            return False 
        head1 = head1.next 
        head2= head2.next
    return True 

def main(): 
    list1= LinkedList.LinkedList()
    list2= LinkedList.LinkedList() 
    list1.addFirst(8)
    list1.addLast(3)
    list1.addLast(2) 
    list1.addLast(6) 
    list2.addFirst(8)
    list2.addLast(3)
    list2.addLast(4) 
    print(prefix(list1,list2))
if __name__ == "__main__":
    main() 