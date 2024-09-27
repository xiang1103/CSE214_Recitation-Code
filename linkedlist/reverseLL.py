from LinkedList import * 

#reverse a linked list with theta(n) space  
def reverse(list):
    output = LinkedList() 
    head= list.head 
    while head is not None: 
        output.addFirst(head.val)
        head = head.next 
    return output  

#reverse a linkedlist in place with theta (1) space complexity
def reverse_inplace(list): 
    head= list.head 
    prev= None 
    cur= head
    while head is not None: 
        cur= head.next 
        head.next= prev 
        prev= head
        if cur is None:
            list.head = prev
        head= cur
    return list

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
    new_list= reverse_inplace(list)
    new_list.print()


if __name__ == "__main__":
    main() 