class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        n = len(nums)
        for i in range(n):
            res.append(nums[(i-k)%n])
        nums[:] = res