class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == " " or len(s) == 1:
            return 1

        s = list(s)
        sub = []
        max_length = 0

        for index in xrange(len(s)):

            for letter in s[index:]:

                if letter not in sub:
                    sub.append(letter)
                else: 
                    if len(sub) > max_length: max_length = len(sub)
                    sub = []
                    break

        return max_length