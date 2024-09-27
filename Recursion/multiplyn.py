#recitation 4, show al multiples of sqrt (n) 

import math 
def body(num):
    sqrtn= (int) (math.sqrt(num))
    recurse(num, sqrtn, 0)

def recurse (num, sqrt, counter):
    if counter> num: return 
    if counter%sqrt ==0: print(counter)
    recurse(num, sqrt, counter+1)

def main(): 
    body(10)
if __name__ =="__main__":
    main() 