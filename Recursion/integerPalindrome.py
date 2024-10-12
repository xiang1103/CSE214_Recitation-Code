#design a recursive algorithm to determine if an integer is palindrome 
def palindrome (x:int) -> bool:
    if x<0: return False 
    divider= 1
    while x>divider *10: 
        divider *=10
    return recursive (x, divider)

def recursive (x:int, divider:int) -> bool: 
    if x ==0: return True 
    right= x%10 
    left= x//divider
    if (right!=left): return False 
    return recursive((x%divider) //10, divider/100)

def main():
    print(palindrome(1231))

if __name__ == "__main__":
    main() 
