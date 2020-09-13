class Solution:
    def getRow(self, k: int) -> List[int]:
        dp = []
        dp.append([1])
        for i in range(1,k+1):
            arr = [1]
            for j in range(len(dp[i-1])-1):
                arr.append(dp[i-1][j]+dp[i-1][j+1])
            arr.append(1)
            dp.append(arr)
        return dp[k]