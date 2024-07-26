# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    p_array, s_array = [0] * 26, [0] * 26
    res = []

    for char in p:
        idx = ord(char) - ord('a')
        p_array[idx] += 1
    
    for char in s[:len(p)]:
        idx = ord(char) - ord('a')
        s_array[idx] += 1
    
    matched = sum([1 if p_array[i] == s_array[i] else 0 for i in range(len(p_array))])

    if matched == 26:
        res.append(0)

    for i in range(len(p), len(s)):
        prev_char_idx = ord(s[i-len(p)]) - ord('a')
        if s_array[prev_char_idx] == p_array[prev_char_idx]:
            matched -= 1
        elif s_array[prev_char_idx] - 1 == p_array[prev_char_idx]:
            matched += 1
        s_array[prev_char_idx] -= 1

        nxt_char_idx = ord(s[i]) - ord('a')
        if s_array[nxt_char_idx] == p_array[nxt_char_idx]:
            matched -= 1
        elif s_array[nxt_char_idx] + 1 == p_array[nxt_char_idx]:
            matched += 1
        s_array[nxt_char_idx] += 1

        if matched == 26:
            res.append(i - len(p) + 1)
    
    return res