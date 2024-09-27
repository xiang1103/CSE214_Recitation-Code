import LinkedList 

#Recitation 2 linked list subsuffix, sublist problem 

#L2 is sublist of L1 if  all elements in L2 appears consecutively in L1 


#time complexity: list1's length is n; list2's length is k: O((n-k+1)(k)); 
                    #not theta because best case is the first few elements match, so O(1)
def isSublist(list1, list2):
    head1= list1.head 
    head2= list2.head 
    if head1 is None and head2 is None: return True 
    len1= find_length(list1)
    len2= find_length(list2)
    if len1<len2: return False  #corner cases where list 1 is smaller than list 2
    counter= 0 
    while (head1!= None): 
        if head1.val == head2.val: 
            dummy1= head1 
            dummy2= head2 
            while dummy2!= None: 
                if dummy2.val!= dummy1.val:
                    break 
                dummy1= dummy1.next 
                dummy2= dummy2.next 
            return True 
        head1= head1.next
        counter+=1 
        if len1 - counter< len2:    #when we run out of things to test 
            return False 
    return False 


def find_length(list):
    head= list.head 
    length=0 
    while head!= None: 
        length+=1 
        head= head.next 
    return length  


#incorrect code provided by recitation 
def sublistRecite(list1,list2): 
    head1 = list1.head 
    head2= list2.head 
    if head1 is None and head2 is None: return False 
    if head1 is None and head2 is None: return False 
    ptr1 = head1 
    ptr2 = head2 
    while ptr2 is not None: 
        ptr2= head2 
        while ptr1 is not None: 
            if ptr2 is None: return False 
            if ptr1.val == ptr2.val: 
                ptr1= ptr1.next 
                ptr2 = ptr2.next 
            else: break 
        if ptr1 is None: return True 
        ptr1 = head1 
        head2 = head2.next 
    return False 


def main(): 
    list1= LinkedList.LinkedList()
    list2= LinkedList.LinkedList() 
    list1.addFirst(8)
    list1.addLast(3)
    list1.addLast(2) 
    list1.addLast(6) 
    list2.addLast(3)
    list2.addLast(2)
    print(sublistRecite(list1,list2))
if __name__ == "__main__":
    main() 