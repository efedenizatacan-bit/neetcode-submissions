class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix
        
        smallest = strs[0]

        for item in strs:
            if item < smallest:
                smallest = item
        

        for i in range(len(smallest)):
            known = []
            for item in strs:
                known.append(item[i])
            for j in range(len(known) - 1):
                if known[j] != known[j + 1]:
                    return prefix
            else:
                prefix += known[0]
        
        return prefix

        