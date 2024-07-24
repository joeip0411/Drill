# https://leetcode.com/problems/encode-and-decode-tinyurl/

# We can also consider including characters as the key to increase the size of the hashmap
class Codec:

    def __init__(self):
        self.hash_map = {}
        self.hash_key = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.hash_map[self.hash_key] = longUrl
        
        short_url = 'http://tinyurl.com/' + str(self.hash_key)
        self.hash_key += 1

        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        hash_key = int(shortUrl[19:])
        res = self.hash_map[hash_key]
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))