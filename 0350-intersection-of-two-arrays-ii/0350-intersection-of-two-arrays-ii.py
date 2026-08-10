class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for elements in nums1:
            c = Counter(nums1)
            output = []

            for n in nums2:
                if c[n] > 0:
                    output.append(n)
                    c[n] = c[n] - 1

            return output
