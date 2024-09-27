#recitation 4. Check if a number is a prime number
import math


def recurseMain(num):
    if num<= 1:
        return False    #corner case 
    if num ==2 or num==3: 
        return True 
    return recurse(num, (int) (math.sqrt(num))) 

def recurse(num, divisor):
    if divisor ==1: 
        return True 
    if num%divisor ==0: 
        return False 
    return recurse(num,divisor-1)


#iterative way 
def norecurse(num):
    if num<=1: 
        return False 
    for i in range(2,(int)(math.sqrt(num))+1):
        if num%i==0: 
            return False 
    return True 

def main(): 
    #print(norecurse(9))
    print(math.sqrt(5))

if __name__ == "__main__":
    main() 