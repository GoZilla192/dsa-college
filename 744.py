class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_letter = "{"  # because '{' > 'z'

        for letter in letters:
            if letter > target:
                min_letter = min(letter, min_letter)

        return min_letter if min_letter != "{" else letters[0]
