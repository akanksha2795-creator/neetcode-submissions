class Solution:
    def climbStairs(self, n: int) -> int:
        prev,curr=1,1
        for i in range(n-1):
            new_var=prev+curr
            prev=curr
            curr=new_var
        return curr

        