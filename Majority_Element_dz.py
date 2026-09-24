#Majority Element
def majority_element(arr: list)->int:
    n=len(arr)
    for x in arr:
        if arr.count(x) > n//2:
            return x
    return -1
print("Введите k и n через пробел:")
k,n =map(int,input().split())
print(f"Введите {k} массивов по {n} чисел:")
result=[]

for i in range(k):
    arr=list(map(int,input().split()))
    result.append(majority_element(arr))

print("\nРезультаты:")
print(*result)