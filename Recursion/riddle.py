#what does the code compute? 
# answer: the smallest element in an array

def Riddle(A,n): 
    if n==1: return A[0]
    else: 
        temp = Riddle(A,n-1)
        if temp<= A[n-1]: return temp 
        else: return A[n-1]

def main(): 
    A= [4,3,2]
    print(Riddle(A, len(A))) 

if __name__ =="__main__":
    main() 
