class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        def merge(left, right):
            res = []
            i=j=0
            while i < len(left) and j < len(right):
                if left[i]<=right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        sorted_nums = merge_sort(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] != i:
                return i
        
        return len(nums)