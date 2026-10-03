# [0. longest-valid-parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

**Difficulty:** `Medium` | **Tags:** `Algorithms` | **Date Solved:** `2026-10-03`

---

## Problem Statement



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
Two-pass scanning (left-to-right and right-to-left) with left/right parenthesis counters.

