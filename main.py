"""
给你一个字符串 s，找到 s 中最长的 回文 子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        max_len = 1
        max_start = 0
        for i in range(n):
            # 检查奇数长度的回文
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            current_len = r - l - 1
            if current_len > max_len:
                max_len = current_len
                max_start = l + 1
            # 检查偶数长度的回文
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            current_len = r - l - 1
            if current_len > max_len:
                max_len = current_len
                max_start = l + 1
        return s[max_start : max_start + max_len]
