class Solution:
    def sort012(self,arr,n):
        # code here
        c0=0
        c1=0
        c2=0
        for i in range(n):
            if arr[i] == 0:
                c0 += 1
            elif arr[i] == 1:
                c1 += 1
            else:
                c2 += 1
        i = 0
        while c0>0:
            arr[i] = 0
            c0 -= 1
            i +=1
        while c1>0:
            arr[i] = 1
            c1 -= 1
            i += 1
        while c2>0:
            arr[i] = 2
            c2 -= 1
            i += 1
        return arr
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends