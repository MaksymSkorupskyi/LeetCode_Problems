# Write a function to find the longest common prefix string amongst an array of strings.

# var 1: zip

class Solution:
    def longestCommonPrefix(self, strings):
        prefix = ''
        for zipp in zip(*strings):
            if len(set(zipp)) != 1:
                break
            prefix += zipp[0]
        return prefix
        # return ''.join([zipp[0] for zipp in zip(*strings) if len(set(zipp)) == 1]) # one liner

# var 2: brute-force for + while
#
# import re
# class Solution:
#     def longestCommonPrefix(self, strings):
#         """
#         :type strings: List[str]
#         :rtype: str
#         """
#         if not strings: # or strings[0] == '':
#             return ''
#         prefix = strings[0]
#         for i in range(1, len(strings)):
#             match = re.match(prefix, strings[i])
#             while not match:
#                 prefix = prefix[:-1]
#                 match = re.match(prefix, strings[i])
#         return prefix

def main():
    a = Solution()
    print(a.longestCommonPrefix([]), [])
    print(a.longestCommonPrefix(['']), [''])
    print(a.longestCommonPrefix(["",""]), ["",""])
    print(a.longestCommonPrefix(["", "b"]), ["", "b"])
    print(a.longestCommonPrefix(["aa","ab"]), ["aa","ab"])
    print(a.longestCommonPrefix(["aa","aa"]), ["aa","aa"])
    print(a.longestCommonPrefix(["a", "a", "b"]), ["a", "a", "b"])
    print(a.longestCommonPrefix(["aac", "a", "ccc"]), ["aac", "a", "ccc"])
    print(a.longestCommonPrefix(["aac", "acab", "aa", "abba", "aa"]), ["aac", "acab", "aa", "abba", "aa"])
    print(a.longestCommonPrefix(["flower", "flow", "flight"]), ["flower", "flow", "flight"])


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')