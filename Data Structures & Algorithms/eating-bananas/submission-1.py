class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        ret = right

        while left <= right:
            k = left + ((right - left) // 2)
            sum = 0
            for p in piles:
                sum += math.ceil(p / k)
            if sum <= h:
                ret = k
                right = k - 1
            else:
                left = k + 1
        return ret