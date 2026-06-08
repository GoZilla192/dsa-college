# Solution #1
# 1. создаем масив expected из отсортированых по неубыванию елементов heights
# 2. проходимся по каждому индексу если елементи отлечаются то увеличиваем ans на 1 
# Time: O(n log n + n), Space: O(n)
class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1

        return ans


# Solution #2
# через list comprehension
# Time: O(n log n + n), Space: O(n)
class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        return sum([1 for i in range(len(heights)) if heights[i] != expected[i]])
