class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        return_list = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if is_palindrome(words[i],words[j]) == True:
                    return_list.append([i,j])
                if is_palindrome(words[j],words[i]) == True:
                    return_list.append([j,i])
        return return_list

        
def is_palindrome(words_one,words_two):
        words_total = words_one + words_two
        left = 0
        right = len(words_total) - 1
        while (left < right):
            if words_total[left] != words_total[right]:
                return False
            else:
                left += 1
                right -= 1
        return True