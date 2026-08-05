class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101
        for h in heights:
            count[h] = count[h] + 1

        sort = []

        for h in range(1, 101):
            c = count[h]
            for j in range(c):
                sort.append(h)

        res = 0
        for i in range(len(heights)):
            if heights[i] != sort[i]:
                res = res + 1

        return res