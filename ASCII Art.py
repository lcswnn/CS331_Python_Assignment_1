class Solution:
    def ascii_art_gen(self, chars):
        for i in range(len(chars)-1):
            pivot_idx = len(chars)-1-i
            seg_a = chars[-1:pivot_idx:-1]
            seg_b = chars[pivot_idx:]
            final = seg_a + seg_b
            print(final)
        for j in range(len(chars)):
            pivot_idx = j
            seg_a = chars[-1:pivot_idx:-1]
            seg_b = chars[pivot_idx:]
            final = seg_a + seg_b
            print(final)


a = Solution()
a.ascii_art_gen('abcde')