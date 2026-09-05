class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        if digits[len(digits) - 1] < 9:
            digits[len(digits) - 1]+=1
            return digits
        else:
            for i,digit in enumerate(digits):
                power = len(digits) - 1 - i
                total+=digit * pow(10, power)

            total+=1

            return [int(item) for item in str(total)]
         