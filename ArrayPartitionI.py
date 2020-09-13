class Solution:
    def arrayPairSum(self, arr: List[int]) -> int:
        arr = sorted(arr)
        n = len(arr)
        sum_ = 0
        for i in range(0,n-1,2):
            sum_+=min(arr[i],arr[i+1])
        return sum_