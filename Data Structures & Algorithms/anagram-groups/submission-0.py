class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for st in strs:
            freq = [0] * 26
            for c in st:
                freq[ord(c) - ord('a')] += 1
            hashmap[tuple(freq)].append(st)
        return list(hashmap.values())