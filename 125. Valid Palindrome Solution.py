import re
class Solution:
    def isPalindrome(self, s: str) -> bool:     # Suppose, s = "My name is Shuchita."
        s = s.upper()                           # making it suitable for classless comaparision. Now s = "MY NAME IS SHUCIHTA."
        s = re.sub(r'[^\w]', '', s)             # removing all puntuation and whitspace.Now s = "MYNAMEISSHUCHITA"
        rev_s = reversed(s)                     # rev_s = "AITAHCUSSIEMANYM" 
       
        if list(s) == list(rev_s):              
            return True
        return False
        
        
