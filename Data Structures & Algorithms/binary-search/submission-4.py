class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            head = left + ((right - left) // 2)

            if target < nums[head]:
                right = head - 1
            elif target > nums[head]:
                left = head + 1
            else:
                return head

        return -1