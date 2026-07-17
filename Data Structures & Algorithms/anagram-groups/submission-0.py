# criar um map para organizarmos nossas listas de anagramas
# para cada string a gente cria um array de letras
# contamos a quantidade de letras da string por meio deste array
# para contar a quantidade de letras podemos usar a funcao ord(letra) diminuindo o valor de ord("a")
# ficando assim, por exemplo:
# se a letra "a" tem o ascii 80 e queremos mapear para 0 no nosso array basta diminuir ord("a")
# como todas as letras minusculas tem o ascii crescente na ordem, diminuir o ord("a") ira resultar num intervalo de 0 a 25
# essa quantidade vira a chave do nosso hashmap
# retornamos o valor do hash

# consideracoes, caso nao exista o valor no hash podemos resolver de duas formas 
# com um if adicionando uma lista com o elemento
# usando defaultdict comecando com list (usaremos essa)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resposta = defaultdict(list) #hash de lista dos anagramas

        for palavra in strs:
            count = [0] * 26 # a ... z

            for char in palavra:
                count[ord(char) - ord("a")] += 1
            
            resposta[tuple(count)].append(palavra) # transforma em tupla pois lista nao pode ser chave de lista
        
        return list(resposta.values())