def rearrange(arr, n):
    temp = 0
    for i in range(n):
        if arr[i]>=0:
            continue
        else:
            r = arr[temp]
            arr[temp] = arr[i]
            arr[i] = r
            temp += 1
    print(arr)


# Driver code
#arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
arr=list(map(int,input().strip().split()))
n = len(arr)
rearrange(arr, n)