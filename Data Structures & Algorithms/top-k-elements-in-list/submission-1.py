# criar um hashmap onde a chave é numero e o valor é sua frequencia no array
# percorrer o array adicionando +1 ao numero
# percorrer o map adicionando a lista de respostas apenas o que tiver valor maior ou igual a k

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        res = []
        for num in nums:
            frequency_map[num] = 1 if num not in frequency_map else  frequency_map[num] + 1
        
        # Sort the items based on frequency in descending order
        sorted_items = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        
        # Take the first k elements from the sorted list
        for i in range(k):
            res.append(sorted_items[i][0])

        return res
