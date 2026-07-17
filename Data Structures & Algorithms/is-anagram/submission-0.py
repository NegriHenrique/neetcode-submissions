# criaremos um hash com a quantidade de letras da string s
# ao percorrer a string t vamos removendo os valores do hash
# se todo o hash estiver zerado retornamos true

# porem aqui a gente usa O(s + t) no espaco, e nao queremos isso

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False

        mapS, mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = 1 if s[i] not in mapS else mapS[s[i]] + 1
            mapT[t[i]] = 1 if t[i] not in mapT else mapT[t[i]] + 1

        return mapS == mapT
