#implement bubble sort 



def bubblesort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return  

def main():
    arr= [3,1,5,6,2,7,8,4]
    bubblesort(arr)
    for num in arr:
        print(num)

if __name__ == "__main__":
    main() 
    