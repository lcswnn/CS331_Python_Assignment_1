class Solution:

    def isPalindrome(self, x: int) -> bool:
        my_int = x
        int_String = str(my_int)
        int_length = len(int_String)
        list = [int(x) for x in str(my_int)]
        i = 0
        p = 0
        q = int_length-1
        while i < int_length:
            if list[p] == list[q]:
                truth_Value = True
                p = p + 1
                q = q - 1
                i = i+1
            elif x == 0:
                truth_Value = True
            else:
                truth_Value = False
                i = i+1

        print(truth_Value)


a = Solution()
a.isPalindrome(0)




