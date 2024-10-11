#reverse an array in place 

#iterative method
def reverseIn(A):
    start=0 
    end= len(A)-1 
    while (start<end):
        temp= A[start]
        A[start]= A[end]
        A[end]= temp
        start+=1 
        end-=1 

#recursive method
def recursive(A):
    if len(A)==1: return 
    return reverseRecurse(A,0, len(A)-1)

def reverseRecurse (A, start, end):
    if start>= end: return 
    temp = A[start]
    A[start] = A[end] 
    A[end] = temp 
    start+=1
    end-=1
    return reverseRecurse(A, start, end)


def main(): 
    A=[1,2,3,4]
    recursive(A)
    for num in A: print(num)

if __name__ == "__main__":
    main()
