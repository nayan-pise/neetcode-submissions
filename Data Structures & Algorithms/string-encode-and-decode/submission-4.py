import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "#"      # changed

        nlist = []
        for word in strs:
            nw = ""
            for char in word:
                if char == "t":
                    nw += "#t"
                elif char == "#":
                    nw += "##"
                else:
                    nw += char
            nlist.append(nw)
        return "t".join(nlist)

    def decode(self, s: str) -> List[str]:
        if s=="#":
            return []
 
        cl = []
        word = ""
        notskip = True

        for char in s:
            if notskip and char == "t":
                cl.append(word)
                word = ""
            elif notskip and char == "#":
                notskip = False
            else:
                notskip = True
                word += char

        cl.append(word)
        return cl
