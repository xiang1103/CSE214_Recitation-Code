def subarray(arr1, arr2):
    if len(arr2)>len(arr1):
        return False 
    if len(arr2)==0: 
        return True 

    diff=len(arr1)- len(arr2)
    counter=0 
    while counter<diff:
        if arr1[counter]== arr2[0]:
            dummy= counter 
            for i in range (0, len(arr2)):
                if arr2[i] != arr1[dummy]:
                    break 
                dummy+=1 
            return True 
        counter+=1 
    return False 


def main(): 
    A1= [1,3,51,5,2,1,3,5]
    A2= [3,5]
    print(subarray(A1,A2))

if __name__ == "__main__":
    main() 