# https://leetcode.com/problems/happy-number/

def isHappy(n: int) -> bool:
    hash_set = set()

    while n != 1:
        temp = n
        res = 0
        
        while temp > 0:
            res += (temp % 10)**2
            temp = temp // 10

        if res in hash_set:
            return False

        hash_set.add(res)
        n = res
        
    return True