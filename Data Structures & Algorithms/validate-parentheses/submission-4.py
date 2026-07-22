# percorre a string
# cria um contador de fechamento
# para cada caractere da string, se for um de abertura ('(', '{', '[') soma no contador
# se for de fechamento (')', '}', ']') , subtrai do contador
# retorna contador == 0
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True

        count_open, count_closes = deque(), deque()


        for char in s:
            ord_char = ord(char)
            open_chars = [ord('('), ord( '{'), ord('[')]
            closes_chars = [ord(')'), ord('}'), ord(']')]


            if ord_char in open_chars:
                count_open.append(char)
            elif ord_char in closes_chars and len(count_open) > 0 :
                last_open = count_open[-1]
                if ord(last_open) == ord('(') and ord_char == ord(')') or ord(last_open) == ord('{') and ord_char == ord('}') or ord(last_open) == ord('[') and ord_char == ord(']'):
                    count_open.pop()
                else:
                    count_closes.append(char)
            else:
                return False


        return len(count_open) == 0 and len(count_closes) == 0