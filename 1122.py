from collections import Counter
from typing import List

# 1. создаем counter (хешмапа, которая сохраняет елемент и его частоту)
# 2. перебираем елементы из arr2 и добавляем столько елементов в результирующий массив сколько есть в counter
# 3. зануляем counter[num]
# 4. далее берем елементы из arr1 которых нету в arr2
# Time: O(n + m), Space: O(n)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        counter = Counter(arr1)
        
        for num in arr2:
            for _ in range(counter[num]):
                result.append(num)

            counter[num] = 0  
            

        unsorted_result_2 = []
        
        for num in arr1:
            if counter[num] != 0:
                unsorted_result_2.append(num)


        return result + sorted(unsorted_result_2)