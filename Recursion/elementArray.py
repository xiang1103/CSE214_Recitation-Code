#a recursive method to check if an element k exists in an array

def recursive(A,n, k):
    if n==1: 
        if A[0] ==k: return True 
        else: return False 
    if A[n-1] ==k: 
        return True 
    else: 
        return recursive(A,n-1, k)

def main(): 
    A=[1,2,3,4]
    k= 0
    print(recursive(A,len(A),k))

if __name__ == "__main__":
    main() 