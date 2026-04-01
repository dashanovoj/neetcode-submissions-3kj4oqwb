class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in result:
                result[tuple(count)] = [str]
            else:
                result[tuple(count)].append(str)
        return list(result.values())
        