#recitation problem: given a stack, reverse it 

def reverse(S):
    output=[] 
    while len(S)>0:
        output.append(S.pop())
    return output

def main(): 
    S=[1,2,3,4]
    S=reverse(S)
    for num in S:
        print(num)

if __name__ == "__main__":
    main() 