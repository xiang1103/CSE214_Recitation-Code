#code to implement hoare partition 

#given array, use the first element as the pivot and paritition so that all elements to the left are smaller, right are bigger 


def hoare(arr, low,high):    #arr: array to be partitioned   #i: beginning index of the array  j:end index of the array 
    pivot= arr[low]   #first element as pivot 
    i=low 
    j=high+1    #we need to shift j so that we can make them at the correct index inside the loop call
    while (True):
        j-=1    #shift j so that j is now in bounds 
        while (arr[j]>pivot):   #move pointer j until the first element that's smaller or equal to pivot (equal to for duplicates)
            j-=1 
        i+=1    #same reason as shifting j 
        while (arr[i]<pivot):   #move i to the first element that's bigger or equal to pivot 
            i+=1 
        if (i>=j):  #if j passed i, meaning everything to the right of i is bigger, so we don't do any shifting
            arr[j],arr[low] =pivot, arr[j]
            return j
        arr[i],arr[j] = arr[j],arr[i]   #swap arr[i] with arr[j] 
        
    

def main():
    #example array: [3,7,5,4,2]
    arr= [3,7,5,4,2]
    hoare(arr,0,len(arr)-1)
    for num in arr: 
        print(num)


if __name__ == "__main__":
    main() 