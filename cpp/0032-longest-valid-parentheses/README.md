# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

**Difficulty:** `Hard` | **Tags:** `String`, `Dynamic Programming`, `Stack` | **Date Solved:** `2026-09-30`

---

## Problem Statement

Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses substring*.

### Example 1:
```text
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

### Example 2:
```text
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

### Example 3:
```text
Input: s = ""
Output: 0
```

### Constraints:
* `0 <= s.length <= 3 * 10^4`
* `s[i]` is `'('`, or `')'`.

---

## Solution (C++)

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(1)`
* **Performance:** `0 ms` (Beats `100.00%`)

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = 0, maxLen = 0;
        int n = s.length();
        
        // Left to right pass
        for (int i = 0; i < n; ++i) {
            if (s[i] == '(') left++;
            else right++;
            
            if (left == right) {
                maxLen = max(maxLen, 2 * right);
            } else if (right > left) {
                left = right = 0;
            }
        }
        
        // Right to left pass
        left = right = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == '(') left++;
            else right++;
            
            if (left == right) {
                maxLen = max(maxLen, 2 * left);
            } else if (left > right) {
                left = right = 0;
            }
        }
        
        return maxLen;
    }
};
```

### Key Intuition
Two-pass linear scan with `left` and `right` counters without extra stack overhead:
1. Left-to-right handles cases where closing parentheses exceed opening ones.
2. Right-to-left handles cases where opening parentheses exceed closing ones (e.g. `"(()"`).
