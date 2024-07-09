from typing import List


# add metadata to the string, i.e. length of each word and number of words
class Solution:

    def encode(self, strs: List[str]) -> str:

        word_len = '#' + '#'.join(str(len(i)) for i in strs)
        list_len = '#' + str(len(strs))
        meta = word_len + list_len

        encoded_string = ''.join(strs) + meta

        return encoded_string

    def decode(self, s: str) -> List[str]:

        meta_list = s.split('#')
        word_count = int(meta_list[-1])
        word_len_list = [int(meta_list[i]) for i in range (-word_count-1,-1)]

        res = []

        i = 0
        
        for word_len in word_len_list:
            word = ''
            while word_len > 0:
                word += s[i]
                i+=1
                word_len -= 1
            
            res.append(word)
        
        return res