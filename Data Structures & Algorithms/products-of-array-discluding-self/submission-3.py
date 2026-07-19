# a ideia aqui é ter um array de prefixo, um de sufixo e um de solucao
# o array de prefixo vai multiplicar com o valor i-1 do array para i > 0 e i para i == 0
# o array de sufixo irá multiplicar o valor de i+1 do array para i < len(nums) e i para len(nums)
# ao final disso basta multiplicar o prefixo e sufixo que dará o resultado
# pref[0] e suf[len(nums) - 1] = 1


# exemplo:
# nums  =   [1,2,4,6]
# prefix =  [1,1,2,8]
# postfix = [48,24,6,1]
# solucao = [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = [0] * length
        sulf = [0] * length
        res = [0] * length

        pref[0] = sulf[length - 1] = 1

        for i in range(1, length):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(length-2, -1, -1):
            sulf[i] = nums[i+1] * sulf[i+1]
        for i in range(length):
            res[i] = sulf[i] * pref[i]
        
        return res