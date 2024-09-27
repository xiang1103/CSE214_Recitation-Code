#determine if a number is power of 2 

def recurse(num):
    if num==1: return True
    elif num%2!=0: return False 
    else: 
        return recurse(num/2)
    
def isPowerOfTwo(n: int) -> bool:
    if n==1: return True 
    elif n<1 or n%2!=0: return False 
    return recurse(n)

def iterative(n):
    if n<1: return False 
    while (n<1):
        if n%2!=0: return False 
        n= n//2 
    return True 
    
def main(): 
    print(isPowerOfTwo(99))

if __name__ == "__main__":
     main() 