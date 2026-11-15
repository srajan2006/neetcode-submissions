class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        def merge(left, right):
            result = []
            i=j=0
            while i<len(left) and j<len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        sorted_nums = merge_sort(nums)

        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False  