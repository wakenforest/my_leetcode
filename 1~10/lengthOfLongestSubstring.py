# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lgstr=[]
        curLen=0
        maxLen=0
        for i in range(len(s)):
            val=s[i]
            if val not in lgstr:
                lgstr.append( val )
                curLen=curLen+1
            else:
                idx=lgstr.index( val )
                lgstr=lgstr[idx+1:]
                lgstr.append(val)
                curLen=len(lgstr)
            if curLen > maxLen:
                maxLen = curLen
        return maxLen

def main():
    # str_uut = 'abcdabcdeabc'
    str_uut = 'abcabcbb'
    s = Solution()
    mlen = s.lengthOfLongestSubstring(str_uut)
    print(mlen)


if __name__ == '__main__':
    main()
