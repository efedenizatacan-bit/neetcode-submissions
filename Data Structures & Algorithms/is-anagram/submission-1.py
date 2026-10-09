class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = sorted(list(s))
        seen2 = sorted(list(t))

        return seen1 == seen2


        
        