from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(n + k), Space: O(n)
        result = []
        nums1 = self.custom_sort(nums1)
        nums2 = self.custom_sort(nums2)
        
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
                continue

            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            

        return result

    def custom_sort(self, array: List[int]):
        # count sort
        # Time: O(n + k), Space: O(n)
        count = [0 for _ in range(1001)]

        for num in array:
            count[num] += 1

        sorted_array = []
        for i in range(len(count)):
            if count[i]: 
                sorted_array.append(i)
       
        return sorted_array