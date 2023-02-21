class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        p = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[i] = nums[p]
                p += 1
        return p



test_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] # two duplicates, the second 2 and 1 should be removed
# should spit out [1, 2, 3, 4, _, _, _, _]
a = Solution()
a.removeDuplicates(test_list)
