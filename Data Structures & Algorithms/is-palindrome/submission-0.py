# tendo em vista que temos que lidar apenas com os alfanumericos da string
# devemos reorganizar a string apenas com os alfa numericos
# apos isso podemos percorrer a string com dois ponteiros, um no inicio e outro no final
# comparamos o char de left e right se nao for igual retorna imediatamente false
# se passou pela string inteira e nao deu false, retorna true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanned_string = ''.join(char.lower() for char in s if char.isalnum())
        left, right = 0, len(cleanned_string)-1
        while left < right:
            if cleanned_string[left] != cleanned_string[right]:
                return False
            left += 1
            right -= 1
        return True
        