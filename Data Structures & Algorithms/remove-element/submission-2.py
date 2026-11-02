class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        view = 0
        edit = 0

        for i in nums:
            if i != val:
                nums[edit] = nums[view]
                edit += 1

            view += 1
            
        return edit
