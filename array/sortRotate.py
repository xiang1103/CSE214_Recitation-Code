#given an array, return True if the array is in non-decreasing order and rotated for some time 


#recitation 2, slide 3
def rotate(arr):
    rotate= False    #variable we return. We need this to be set to true (look for rotation)
    for i in range(1, len(arr)-1):
        prev= arr[i-1]  
        if arr[i]<prev: #test for rotation 
            if arr[i+1]<arr[i]:
                return False 
            else: 
                rotate= True
        if arr[-1]<arr[-2]:
            rotate = True 
    return rotate 

def findFirstMin(arr):
    index= 0 
    for i in range (1,len(arr)):
        if arr[i]<arr[index]:
            index= i
    return index

#recitation solution 
#this will not work for multiple rotations 
def isSortedAndRotated(arr):
    minIndex= findFirstMin(arr)
    for i in range(0, len(arr)): 
        current= arr[((minIndex+i)%len(arr))] 
        next= arr[((minIndex+i+1)%len(arr))] 
        if current> next: return False 
    return True 
        

def main():
    arr= [4,5,1,2,1,5]
    print(rotate(arr))


if __name__== '__main__':
    main() 