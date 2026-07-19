# ideia trivial --> forca bruta
# para cada elemento do array eu busco o seu subsequente e adiciono a um contador
# se nao achou mais nenhum elemento eu faco o max entre o que a gente ja tinha feito anteriormente e o que pegamos nesse loop
# no final retorna o max
# isso gera uma complexidade O(nˆ2) pois para cada elemento teriamos que percorrer todo o array buscando por o subsequente

# ideia mais inteligente
# ordena todo o array
# faz um loop usando dois ponteiros, um no inicio do intervalo e outro no final
# ve o tamanho right - left > max atual
# e faz isso por todo o array até acabar
# problema aqui: o algoritmo de ordenacao tende a ser O(log n)

# precisamos de uma solucao O(n)

# utilizando hash set
# aqui criamos um set da lista nums
# para cada elemento verificamos se ele e os subsequentes estao no set
# enquanto estiver no set eu salvo uma variavel com a soma dos elementos que ja passaram
# acabou o loop eu faco o max da streak e do que ja tinha no max
# com isso percorremos os elementos da lista apenas uma vez

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) < 1:
            return 0
        nums_in_list = set(nums)
        max_streak = 0
        for num in nums:
            streak = 0
            aux_num = num
            while aux_num in nums_in_list:
                streak += 1
                aux_num += 1
            max_streak = max(max_streak, streak)
        return max_streak
        