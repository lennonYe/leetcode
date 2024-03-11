class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        start_count = False
        final_s = ''
        final_num = 0
        negative_flag = False
        for char in s:
            if char.isdigit() == True:
                start_count = True
                final_s += char
            if start_count == True and char.isdigit() == False:
                break
            if char == '-':
                negative_flag = True
                start_count = True
            if char == '+':
                start_count = True
            if start_count == False and char.isdigit() == False:
                return 0 
        
        if final_s.isdigit() == True:
            final_num = int(final_s)
        else:
            return 0

        
        if negative_flag == True:
            final_num *= -1
        if final_num < -pow(2,31):
            final_num = -pow(2,31)
        elif final_num > (pow(2,31) - 1):
            final_num = pow(2,31) - 1
        return final_num
