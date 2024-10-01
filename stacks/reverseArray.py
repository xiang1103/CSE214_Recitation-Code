#recitation 5, slide 1 
# reverse an array using a stack 

def reverse(A): 
    stack= [] 
    for num in A: 
        stack.append(num)
    for i in range(0, len(stack)):
        A[i]= stack.pop() 
    return A 

def print_arr(A): 
    for num in A: 
        print(num, end=",")

def main(): 
    A=[1,2,3,4]
    B= reverse(A)
    print_arr (B) 

if __name__ == "__main__":
    main() 