#compute the factorial of n, given n 

def iterative(n): 
    output= 1 
    for i in range (n,1,-1):
        output *= i 
    return output
def recursive(n): 
    if n==1: 
        return 1 
    return n* recursive(n-1)



def main(): 
    print(recursive(10))


if __name__ == "__main__":
    main() 