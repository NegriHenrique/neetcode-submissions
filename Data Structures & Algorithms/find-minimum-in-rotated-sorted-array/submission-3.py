# para encontrar o menor numero globalmente, considerando o array ordenado
# basta buscarmos de forma a dividir pela metade o array 
# e verificar se o right < mid, caso sim pegamos o lado direito
# caso contrario sabemos que o menor está no lado esquerdo
# fazemos isso até que right e left sejam iguais e entao acharemos o menor global
# ai basta retornar ele 


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0 
        
        left, mid, right = 0, 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]