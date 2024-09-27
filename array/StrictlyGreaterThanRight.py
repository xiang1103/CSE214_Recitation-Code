#recitation 3 slide 14 

#given an array, print numbers that are strictly greater than all numbers to its right 

def greater(A):
    max=-2*10e3 
    for i in range(len(A)-1, -1, -1):
        if A[i]>max: 
            print(A[i])
            max= A[i] 
    return 


def main():
    A=[]
    greater(A)

if __name__ == "__main__":
    main() 