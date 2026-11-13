class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSort = ''.join(sorted(s))
        tSort = ''.join(sorted(t))
        if sSort == tSort:
            return True
        return False