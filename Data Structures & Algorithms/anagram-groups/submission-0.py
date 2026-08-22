from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hash map to group words by their sorted form
        anagram_map = defaultdict(list)
 
        for word in strs:
            # Sort the word to create a canonical key
            count=[0]*26;
            for char in word:
                count[ord(char)-ord('a')]+=1 
            anagram_map[str(count)].append(word)

        # Return all grouped lists
        return list(anagram_map.values())