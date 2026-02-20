class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            digits[0] += 1
            if digits[0] == 10:
                digits[0] =1
                digits.append(0)
            return digits
        digits[len(digits) - 1] += 1
        if digits[len(digits) - 1] == 10:
            carry = 1
            digits[len(digits) - 1] = 0
            for i in range (len(digits) - 2, -1, -1):
                if carry == 1:
                    digits[i] += 1
                    carry = 0
                    if digits[i] == 10:
                        carry = 1
                        digits[i] = 0
                    
            if digits[0] == 0:
                n = [1,]
                digits = n + digits


        
        return digits
        