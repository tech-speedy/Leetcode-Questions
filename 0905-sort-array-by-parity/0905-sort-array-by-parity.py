class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        output = []
        for a in A:
            if a % 2 == 0:
                output.insert(0, a)
            else:
                output.append(a)

        return output