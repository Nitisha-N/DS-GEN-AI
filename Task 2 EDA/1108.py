#1108. Defanging an IP 

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
