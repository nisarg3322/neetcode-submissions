class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        if s == " ":
            return 1
        
        l = r = 0
        result = 0
        hashset = set()

        for i in range(len(s)):
            r = i
            print("current elem:", s[i])
            if s[r] in hashset:
                # do something
                print("inside in hashset loop", s[r])
                while s[r] in hashset:
                    hashset.discard(s[l])
                    l += 1
                    print("l:", l)
                    print("r:", r)
                hashset.add(s[r])
            else:
                print("adding to hashset", s[r])
                hashset.add(s[r])
                length = r - l + 1
                if length > result:
                    result = length
            print("result:", result)
            print("hashset:", hashset)
                
        return result
