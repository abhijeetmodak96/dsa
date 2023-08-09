class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        self.a = a
        self.size = size
        ##Your code here
        self.sum = 0
        self.total = 0
        for i in self.a:
            self.sum += i
            if self.sum > self.total:
                self.total = self.sum
            if self.sum <= 0:
                #total = 0
                self.sum = 0
        if self.total == 0:
            return self.a[0]
        return self.total
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends