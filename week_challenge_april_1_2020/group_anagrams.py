# Group Anagrams
# group_anagrams.py
# https://leetcode.com/submissions/detail/320993297/

from typing import List
#import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dict = {}
      for s in strs:
          key = list(s)
          key.sort()
          canonical = ''.join(key)
          l = dict.get(canonical)
          if l == None:
            l = []
            dict[canonical] = l
          l.append(s)
      return dict.values()


if __name__ == '__main__':
    obj = Solution()
    data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = obj.groupAnagrams(data)
    print('[')
    comma2 = ''
    for val in result:
        if comma2 != '':
            print(comma2)
        print('['.format(comma2), end='')
        comma2 = ','
        comma = ''
        for x in val:
            print('{0}{1}'.format(comma, x), end='')
            comma = ','
        #[print('{0}{1}'.format(comma, x), end='') for x in result.get(key)]
        print(']', end='')
    print('')
    print(']')
