from collections import Counter
from typing import List

# сортируем массив по возрастанию частоты числа, если частота одинакова то сортируем по числу по убыванию
# Time: O(n log n + n), Space: O(n)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))