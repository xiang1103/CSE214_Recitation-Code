from sort import * 

#recitation 3, slides 6 
#given an array, find the minimum number of elements needed that add up to k
def MinElementsSum(A,k):
    A= sort(A) 
    i= len(A)-1 
    sum=0
    while i>=0:
        sum= sum+A[i]
        if sum>=k:
            return len(A)-i 
        i-=1; 
    return -1 

def main():
    A=[1,4,2,3,5]
    print(MinElementsSum(A,4))

if __name__ == "__main__":
    main()