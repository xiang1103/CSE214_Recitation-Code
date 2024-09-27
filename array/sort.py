#recitation 3 slide 4 
#given one array, sort from least to greatest 

def sort(arr1):
    for i in range(0,len(arr1)-1):
        for j in range(0, len(arr1)-i-1):
            if arr1[j]>arr1[j+1]:
                temp= arr1[j]
                arr1[j]= arr1[j+1]
                arr1[j+1]=temp 
    return arr1 

def main(): 
    A=[5,4,3,2,1]
    A= sort(A)
    for num in A: 
        print(num, end="->")

if __name__== "__main__":
    main() 