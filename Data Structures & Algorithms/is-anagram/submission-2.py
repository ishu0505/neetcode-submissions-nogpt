class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1

            if t[i] in t_hash:
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1
        print(s_hash)
        print(t_hash)
        if s_hash == t_hash:
            return True
        return False

        