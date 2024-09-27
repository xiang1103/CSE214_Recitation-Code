
#recitation 2, Product Besides itself 
def product (arr):
    num_zero= 0
    product= 1 
    for num in arr: 
        if num==0: 
            num_zero +=1
        else: 
            product *=num 
    answer = [0] * len(arr) 
    if num_zero>=2:
        return answer 
    if num_zero==1: 
        for i in range(0, len(arr)):
            if arr[i] ==0:
                answer[i]= product
            else: 
                answer[i] = 0 
    else: 
        for i in range(0, len(arr)):
            answer[i] = product/arr[i] 
    
    return answer 


def main(): 
    arr= [0,1,0,-1]
    output= product(arr)
    for num in output: 
        print (num)

if __name__ == "__main__":
    main() 