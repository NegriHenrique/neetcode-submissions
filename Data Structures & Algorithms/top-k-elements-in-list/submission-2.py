# criar um hashmap onde a chave é numero e o valor é sua frequencia no array
# percorrer o array adicionando +1 ao numero
# percorrer o map adicionando a lista de respostas apenas o que tiver valor maior ou igual a k

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        frequency_list = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)
        
        for num, frequency in frequency_map.items():
            frequency_list[frequency].append(num)
        for i in range(len(frequency_list) - 1 , 0, -1):
            for j in frequency_list[i]:
                res.append(j)
                if len(res) == k:
                    return res
