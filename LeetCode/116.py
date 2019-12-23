class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if(not triangle):
            return 0
        n=len(triangle)
        if(n==1):
            return triangle[0][0]
        for i in range(1,n):
            for j in range(len(triangle[i])):
                if(j==0):
                    triangle[i][j]+=triangle[i-1][j]
                elif(j==len(triangle[i])-1):
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])