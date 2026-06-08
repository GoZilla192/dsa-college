from typing import List


# используем алгоритм сортировки count sort
# Time: O(n + m), n - длина nums, m - максимальная частота какого то числа
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1

        j = 0
        for i in range(len(count)):
            for _ in range(count[i]):
                nums[j] = i
                j += 1
