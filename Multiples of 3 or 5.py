# We are looking for a method that given a positive integer 𝑛, it finds the sum of all the multiples of 3 or 5 below 𝑛.

class Solution:
    def multiples(self, n: int):
        five_tally = 0
        three_tally = 0
        five_list = [n for n in range(1, n) if n % 5 == 0]
        three_list = [n for n in range(1, n) if n % 3 == 0]
        for i in range(0, len(five_list)):
            five_tally = five_tally + five_list[i]
        for j in range(0, len(three_list)):
            three_tally = three_tally + three_list[j]

        print("The total sum of the multiples is: " + str(five_tally + three_tally))

a = Solution()
a.multiples(5)
a.multiples(10)
a.multiples(500)
a.multiples(1000)
a.multiples(333)
