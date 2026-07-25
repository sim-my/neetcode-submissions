class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        org_str = ""
        for char in s[::-1]:
            if char != " " and char.isalnum():
                new_str+=char.lower()

        for char in s:
            if char != " " and char.isalnum():
                org_str+=char.lower()
        
        print(new_str, org_str)
        if new_str == org_str:
            return True
        else:
            return False

