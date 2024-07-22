# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hash_map = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0,
        }

        reverse_map = {
            v:k for k,v in hash_map.items()
        }

        def to_int(num):
            multiplier = 1
            res = 0

            for i in range(len(num)-1,-1,-1):
                res += hash_map[num[i]] * multiplier
                multiplier *= 10

            return res

        num1 = to_int(num1)
        num2 = to_int(num2)

        product = num1 * num2

        if not product:
            return "0"

        res = ''

        while product:
            temp = reverse_map[product % 10]
            res = temp + res
            product = product // 10

        return res

# when multiplying numbers, the digit will be store in position i + j
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                res[i+j] += product
                res[i+j+1] += res[i+j] // 10
                res[i+j] = res[i+j] % 10
                
        res = res[::-1]
        start = 0
        while res[start] == 0:
            start += 1
        
        res = res[start:]

        return ''.join(str(i) for i in res)
