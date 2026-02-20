class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = s.split().pop()
        return len(lastWord)