#recitation 5, slide 2 
#given an array of (), {}, [] check if the parentheses are correct 

def valid(A):
    stack= []  
    for i in range(0, len(A)): 
        if A[i] =='{' or A[i]=='(' or A[i]== '[':
            stack.append(A[i]) 
        elif len(stack)>0:
            if (A[i]== ')' and stack[-1]=='(' ) or (A[i]=='}' and stack[-1]=='{') or (A[i]==']' and stack[-1] =='['): 
                stack.pop() 
            else: 
                return False 
        else: return False 
    return len(stack)==0

def main(): 
    s="({})"
    print(valid(s))

if __name__ == "__main__":
    main() 