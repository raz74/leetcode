class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        text = text.split()
        for item in text:
            if any(letter in brokenLetters for letter in item):
                continue
            else:
                count += 1

        return count


print(Solution().canBeTypedWords('leet code', 'lt'))
