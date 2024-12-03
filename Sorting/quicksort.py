from hoare_partition import * 

#quicksort with hoare_partition 
def quicksort(arr,low,high):
    if (low<high):
        mid= hoare(arr,low,high) 
        quicksort(arr, low,mid-1)
        
        quicksort(arr, mid+1, high)
    return 


def main(): 
    arr= [3,7,5,4,2]
    quicksort(arr,0,len(arr)-1)
    for num in arr: 
        print(num)


if __name__ == "__main__":
    main() 