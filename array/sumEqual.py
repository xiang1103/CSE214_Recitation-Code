def sum1 (arr):
    sum =0 
    for i in range(0, len(arr)):
        sum += arr[i] 
    return sum 

def sum2(arr):
    sum= 1
    for i in range (0,len(arr)-1):
        sum+= arr[i] + 1
    return sum 


def main(): 
    A=[1,2,3,4,5,6,7,8,9,10,11]
    print(sum1(A)==sum2(A))

if __name__ == '__main__':
    main()