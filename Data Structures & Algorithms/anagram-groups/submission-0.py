class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = []
        dici = {}

        for item in strs:
            srtd = tuple(sorted(item))
            if srtd not in dici:
                dici[srtd] = [item]
            else:
                dici[srtd].append(item)
        
        for item in dici:
            main.append(dici[item])
        
        return main


        