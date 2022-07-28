'''
Test if given string is palindrome or not
'''
class Palindrome:
    def __init__(self, l_Array):
        self.lArray = l_Array
        self.fPalindromeTest(l_Array)

    @staticmethod
    def fPalindromeTest(l_Array):
        lPalindrome = 0
        for i in range(0, len(l_Array[::-1])):
            if l_Array[::-1][i] != l_Array[i]:
                lPalindrome = 0
                break
            else:
                lPalindrome = 1

        lString = ''
        if lPalindrome == 1:
            lString = lString.join(l_Array)
            print("{} is a Palindrome".format(lString))
        else:
            lString = lString.join(l_Array)
            print("{} is not a Palindrome".format(lString))
        return 1

lArray = list(('Malayalam').upper())
lArray1 = list(('aabXba').upper())
OPlaindrome = Palindrome(lArray)
OPlaindrome = Palindrome(lArray1)