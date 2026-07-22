# sliding windows variavel
# comecando na atual e expandindo verificando se right esta no set de t
# teremos um hash de letras (a-z ... A-Z) registrando a quantidade de cada letra de t
# teremos um segundo hash que representa as letras da nossa substring
# comecando por left = 0 right = 0 e avancamos ambos até achar a primeira letra que conhena em hash_t
# enquanto hash_substring != hash_t aumentamos right 
# e adicionamos a hash_substring apenas as letras que existem em hash_t
# quando for igual os dois hashs, fazemos uma validacao se a substring é min da substring que ja tinhamos (comecando com s inteiro)
# apos isso avancamos left até hash_substring ser diferente de hash_t

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(t) > len(s):
            return ""
        
        hash_t, hash_substring = {}, {}

        for char in t:
            hash_t[char] = hash_t.get(char, 0) + 1
        
        left = 0
        have, need = 0, len(hash_t)
        res, resLen = [-1, -1], float("infinity")
        
        for right in range(len(s)):
            char = s[right]
            hash_substring[char] = hash_substring.get(char, 0) + 1

            if char in hash_t and hash_t[char] == hash_substring[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = (right - left + 1)
                    res = [left, right]
                hash_substring[s[left]] -= 1
                if s[left] in hash_t and hash_t[s[left]] > hash_substring[s[left]]:
                    have -=1
                left += 1
        
        l, r = res
        return s[l : r+1] if resLen != float("infinity") else ""
        
                

        
        