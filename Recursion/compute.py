def compute(x,y):
    if x==0:
        return y 
    else: 
        return compute(x-1, y*x)
    
def main():
    print(compute(3,2)) 

if __name__ == "__main__":
    main() 