#Convert a decimal numeber to octal 

def recursive(n): 
    if n==0: return ""
    hex= recursive(n//8)
    remainder= n%8 
    return hex + str(remainder) 

def iterative(n):
    hex= ""
    while n>0: 
        remainder= n%8 
        hex= str(remainder) + hex 
        n= n//8 
    return hex 

def main(): 
    print(iterative(34)) 


if __name__ == "__main__":
    main() 