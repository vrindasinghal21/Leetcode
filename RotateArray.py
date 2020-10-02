class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        temp = [0]*k
        for i in range(min(k,n)):
            prev = i
            next_ = i+k
            num = arr[prev]
            t = num
            while(next_<n):
                t = arr[next_]
                arr[next_] = num
                num = t
                next_,prev = next_+k,next_
            temp[next_%n] = t
        for i in range(min(n,k)):
            arr[i] = temp[i]
 def add(a,b):
    x = a+b
    return x
