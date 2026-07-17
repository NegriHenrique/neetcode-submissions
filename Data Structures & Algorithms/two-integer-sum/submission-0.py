# solucao forca bruta
# a cada elemento do array a gente busca pelo restante do array por um valor onde 
# num[i] - target = nums[j]
# O(n²)

# solucao mais inteligente
# a cada elemento do array a gente salva em uma hash o valor necessário para a soma
# exemplo:
# nums = [3,4,5,6], target = 7
# hash = {
#   3: 0
#   4: 1
#   5: 2
#   6: 3
#} 
# fazemos uma validacao se nums[i] está no hash, se sim return [i, hash[target - nums[i]]]
# senao adicionamos o contraposto no hash {[taget - nums[i]]: i}
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        hash_sum = {}

        for i in range(len(nums)):
            target_value = target - nums[i]
            if target_value in hash_sum:
                return [hash_sum[target - nums[i]], i]
            
            hash_sum[nums[i]] = i