from collections import Counter
from typing import List

# проверяем наличия елементов и одниковость их частоты 
# Time: O(n), Space: O(1)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)