class Solution:
    def canJump(self, arr: List[int]) -> bool:
        n = len(arr)
        x = n-1
        for i in range(x,-1,-1):
            if (i+arr[i])>=x:
                x = i
        if x==0:
            return True
        else:
            return False