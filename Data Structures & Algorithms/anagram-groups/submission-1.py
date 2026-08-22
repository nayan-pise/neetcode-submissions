class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagram = {}
        for word in strs:
            key ="".join(sorted(word))#first changing the list into the string by joined menthod then sort the each and every word of the string 
            if key not in Anagram:
                Anagram[key]=[]
            Anagram[key].append(word)
        return list(Anagram.values())