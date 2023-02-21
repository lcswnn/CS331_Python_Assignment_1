class Solution:
    def numberOfWords(self, a: str):
        print(len(a.split(" ")))

a = Solution()
a.numberOfWords("It’s a closed-book-closed-notes exam.")
a.numberOfWords("How much money do you have? -50 dollars.")
a.numberOfWords("www.google.com is a website.")
a.numberOfWords("Academic Calendar\nAcademic Programs- Graduate\nAcademic Programs- Undergraduate")