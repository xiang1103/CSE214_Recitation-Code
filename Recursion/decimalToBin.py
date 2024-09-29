#recitation 4 slide 1 
#convert a number from decimal to binary in both recursive and non-recursive way 

def recursive(decimal):
    if decimal ==0: return "" 
    binary = recursive(decimal//2)
    remainder= decimal%2 
    return binary + str(remainder)

def iterative(decimal):
    binary= ""
    while decimal>0: 
        remainder= decimal%2
        binary = str(remainder) + binary 
        decimal = decimal//2 
    return binary 
def main(): 
    print(iterative(28))


if __name__=="__main__":
    main() 