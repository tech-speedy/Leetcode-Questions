class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = list(set(nums))

        res = sorted(temp, reverse = True)
        if(len(res) < 3):
            return res[0]
        else:
            return res[2]