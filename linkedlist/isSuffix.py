import LinkedList 


#Recitation 2, Linkedlist problem 

# list 2 is the suffix of list 1 if list2's nodes are the same as list1's last nodes (same length)
def isSuffix(list1, list2):
    head1 = list1.head 
    head2= list2.head 
    len1= find_length(list1)
    len2 = find_length(list2)
    if (len2 > len1):
        return False 
    index= len1-len2    #index where the suffix starts 
    length=0
    while (length<index):   #TODO: potential bug of index errors 
        length+=1
        head1 = head1.next 
    while (head2!=None):
        if (head2.val!=head1.val):
            return False 
        head1= head1.next 
        head2= head2.next 
    return True  
        

def find_length(list):
    head= list.head 
    length=0 
    while head!= None: 
        length+=1 
        head= head.next 
    return length  

def main(): 
    list1= LinkedList.LinkedList()
    list2= LinkedList.LinkedList() 
    list1.addFirst(8)
    list1.addLast(3)
    list1.addLast(2) 
    list1.addLast(6) 
    list2.addFirst(8)
    list2.addLast(3)
    list2.addLast(2)
    list2.addLast(6)
    print(isSuffix(list1,list2))
    
if __name__ == "__main__":
    main() 