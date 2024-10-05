#given an sorted stack and return 1 if the element exists in the stack, -1 if not

def search(S,k):
    while len(S)>0:
        if S[-1]<k:
            return -1 
        if S[-1] ==k:
            return 1 
        S.pop() 
    return -1 

def main():
    S=[1,2,3,4]
    print(search(S,2))

if __name__ == "__main__":
    main() 