#predict the output of the following code:
def Q(n): 
    if n==1: return 1 
    return Q(n-1) + 2*n-1 

def main(): 
    print(Q(6))

if __name__ =="__main__":
    main() 
    