class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            sum_el = numbers[l] + numbers[r]

            if sum_el == target:
                return (l + 1, r + 1)
            elif sum_el > target:
                r -= 1
            elif sum_el < target:
                l += 1
