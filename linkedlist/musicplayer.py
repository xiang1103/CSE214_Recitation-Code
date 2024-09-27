from LinkedList import * 

#recitation 3, slide 7

#play the playlist infinite number of times; use print as play music 
def playUnlimited(list): 
    head= list.head 
    cur= list.head 
    while head: 
        print(cur.val)
        if cur.next is None: 
            cur=head
        else: 
            cur=cur.next 
    return 

#insertion sort of linked list
def insertionSort(list):
    head= list.head 
    dummy= Node(0)
    dummy.next= head 
    lastsorted= head 
    cur= head.next 
    while (cur is not None):
        if lastsorted.val<=cur.val:
            lastsorted= lastsorted.next 
        else:
            prev=dummy 
            while prev.next.val<=cur.val: 
                prev= prev.next 
            lastsorted.next= cur.next 
            cur.next= prev.next 
            prev.next= cur 
        cur= lastsorted.next 
    list.head= dummy.next 
    return list 
    
#move the last k songs to the front of the list 
def rotatePlaylist(list, k):
    #corner case of empty list or k =0 
    head= list.head 
    if (head is None or head.next is None or k==0):
        return list 
    endNode = head 
    length=1 
    while endNode.next is not None:
        length+=1 
        endNode= endNode.next 
    endNode.next= head 
    k= k % length   #handle the case if k is more than the length 
    step_to_head= length-k
    while step_to_head>0: 
        endNode= endNode.next 
        step_to_head-=1 
    list.head= endNode.next
    endNode.next= None 
    return list  



     
#remove kth element from the end. Assume kth is not the first 
def removekth(list,k):
    head= list.head 
    cur= list.head 
    i=0 
    while (i<k and cur is not None):
        cur=cur.next 
        i+=1 
    if cur is None: 
        return list 
    slow= head 
    while (cur.next is not None):
        cur= cur.next 
        slow = slow.next 
    slow.next=slow.next.next 
    return list 

def main():
    list= LinkedList() 
    list.addFirst(4)
    list.addLast(2) 
    list.addLast(1) 
    list.addLast(3)
    insertionSort(list)
    list.print() 


if __name__=="__main__":
    main() 

