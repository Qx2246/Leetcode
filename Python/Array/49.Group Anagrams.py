class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            '''
            sorted(word) sorts the letters alphabetically and gives back a list of characters.
            Example: sorted("eat") → ['a','e','t'] AND ''.join(...) glues the characters back into a string.
            "".join(['a','e','t']) → "aet"
            '''
        return list(anagram_map.values())
        
