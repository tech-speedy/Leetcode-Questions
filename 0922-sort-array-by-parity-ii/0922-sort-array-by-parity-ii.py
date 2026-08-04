class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        e = 0
        o = 1
        while e < n and o < n:
            while e < n and nums[e] % 2 == 0:
                e = e + 2
            while o < n and nums[o] % 2 != 0:
                o = o + 2
            if e < n and o < n:
                nums[e], nums[o] = nums[o], nums[e]
                e = e + 2
                o = o + 2

        return nums