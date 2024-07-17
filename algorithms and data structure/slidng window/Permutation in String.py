# https://leetcode.com/problems/permutation-in-string/description/

def checkInclusion(s1: str, s2: str) -> bool:
    hash_map = {}

    for char in s1:
        hash_map[char] = hash_map.get(char, 0) + 1
    
    left = 0
    right = left + len(s1)

    while right <= len(s2):
        long_hash_map = {}

        for i in range(left, right):
            long_hash_map[s2[i]] = long_hash_map.get(s2[i], 0) + 1
        
        if long_hash_map == hash_map:
            return True
        
        left += 1
        right += 1
    
    return False

# Do a full scan of both array at the beginning and calculate matched character
# Iterate through the subsequent chars, update the array and recalculate match
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False
    
    s1_arr = [0 for i in range(26)]
    s2_arr = [0 for i in range(26)]

    for i in range(len(s1)):
        s1_arr[ord(s1[i]) - ord('a')] += 1
        s2_arr[ord(s2[i]) - ord('a')] += 1

    match = sum([s1_arr[i] == s2_arr[i] for i in range(len(s1_arr))])

    if match == 26:
        return True

    for i in range(len(s1), len(s2)):

        remove_idx = ord(s2[i-len(s1)]) - ord('a')
        s2_arr[remove_idx] -= 1

        if s2_arr[remove_idx] == s1_arr[remove_idx]:
            match += 1
        elif s2_arr[remove_idx] + 1 == s1_arr[remove_idx]:
            match -= 1

        add_idx = ord(s2[i]) - ord('a')
        s2_arr[add_idx] += 1

        if s2_arr[add_idx] == s1_arr[add_idx]:
            match += 1
        elif s2_arr[add_idx] - 1 == s1_arr[add_idx]:
            match -= 1

        if match == 26:
            return True

    return False
            