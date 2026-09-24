#Merge Two Sorted Arrays
def merge_arrays(a: list, b: list)-> list:
    result =[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i] <=b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    for k in range(i, len(a)):
        result.append(a[k])
    for k in range(j, len(b)):
            result.append(b[k])    
    return result

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

result= merge_arrays(a,b)
print(*result)