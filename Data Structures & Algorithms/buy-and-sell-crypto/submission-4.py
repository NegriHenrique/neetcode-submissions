# forca bruta
# percorre cada dia verificando o maximo da soma com cada outro dia 
# retorna a soma maxima
# O(nˆ2)

# outra solucao, usar dois ponteiros, um no incio e otro no final, verificar a soma maxima e ir atualizando com a seguinte premissa:
# - se left+1 menor que left, atualizamos left
# - se right-1 for maior que right, atualizamos right

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left=right
                right+=1
                continue

            profit = prices[right] - prices[left]
            
            max_profit = max(max_profit, profit)
            print(prices[left], prices[right], max_profit)
            right+=1

        return max_profit