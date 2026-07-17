# solucao pratica da vida real
# cria um set com os numeros, compara o tamanho do set com a lista, se for diferente return true

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        return len(nums) != len(list(nums_set))
        