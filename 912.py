class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        else:
            mid_idx = len(nums) // 2
            mid = nums.pop(mid_idx)
            left = [x for x in nums if x <= mid]
            right = [x for x in nums if x > mid]

            return self.sortArray(left) + [mid] + self.sortArray(right)
