def check(A):
    #Condition to check if all 1s are together
    b=True
    for i in range(0,len(A)-1):
        if(A[i+1]-A[i]!=1):
            b=False
            break
    return b
def config(arr):
    #Converts original array into an array where elements are positions of
    #1s in the original array.
    # For example: [1,0,1,0,1,1] is converted to [0,2,4,5]
    A=[]
    c=0
    for i in range(len(arr)):
        if(arr[i]==1):
            A.append(i)
            
    return A
            
def pot(A):
    s=0
    #A simple potential is defined as the sum of absolute differences
    #between each and every 1
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            s=s+abs(A[i]-A[j])
    return s

def move(A,i,l,s):#l is length of arr, i is the index of current element
    #Based on the array and the index, we find a way to minimise potential
    #of the array.

    #s is incremented for every move (when A1,the new array, is returned)
    A1=A[:]
    A2=A[:]
    
    if(i==0):
        if(A[1]!=A[0]+1):
            A1[0]=A[0]+1
            if(pot(A1)<pot(A)):
                return (A1,s+1)
            else:
                return (A,s)
        else:
            return (A,s)
    elif(i==len(A)-1):
        if(A[i-1]!=A[i]-1):
            A1[i]=A1[i]-1
            if(pot(A1)<pot(A)):
                return (A1,s+1)
            else:
                return (A,s)
        else:
            return (A,s)

    # i==0 and i==len(A)-1 are special conditions for boundary elements to prevent
    # StackOverflowError
    
    elif(A[i+1]!=A[i]+1 and A[i-1]!=A[i]-1):
        A1[i]=A[i]+1
        A2[i]=A[i]-1
        a=min(pot(A),pot(A1),pot(A2))
        if(a==pot(A)):
            return (A,s)
        elif(a==pot(A1)):
             return (A1,s+1)
        else:
            return (A2,s+1)
    elif(A[i+1]!=A[i]+1):
        A1[i]=A[i]+1
        if(pot(A1)<pot(A)):
            return (A1,s+1)
        else:
            return (A,s)
    elif(A[i-1]!=A[i]-1):
        A1[i]=A1[i]-1
        if(pot(A1)<pot(A)):
            return (A1,s+1)
        else:
            return (A,s)
        
    else:
        return (A,s)
    
      #Basically, if you can swap a 1 with a 0 and if the result's potential
      #is less than the original's, execute the swap.
        
def main(arr):
    A=config(arr)
    c=len(A)
    l=len(arr)
    ctr=0
    s=0
    while(True):
        if(check(A)==True):
           
            print('Minimum Number of Swaps : ',s)
            break
        A,s=move(A,ctr%c,l,s)
        ctr=ctr+1
        
        
    
print('Enter binary string. For example, for [1,0,0,1,1] enter: 10011')
n=(input('Enter binary number: '))
arr=list(n)
arr=list(map(int, arr))
count=0

for i in arr:
    
    if i==1:
        count=count+1
   
main(arr)  
