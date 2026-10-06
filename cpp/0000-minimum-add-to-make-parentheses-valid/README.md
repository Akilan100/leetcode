# [0. minimum-add-to-make-parentheses-valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

**Difficulty:** `Medium` | **Tags:** `Algorithms` | **Date Solved:** `2026-10-06`

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
    int minAddToMakeValid(string s) {
        int openCount = 0;
        int minAdded = 0;
        for (const char& ch : s) {
            if (ch == '(') {
                openCount++;
            } else {
                if (openCount > 0) {
                    openCount--;
                } else {
                    minAdded++;
                }
            }
        }
        return minAdded + openCount;
    }
};
```

### Key Intuition
Single-pass greedy counter tracking unmatched opening and closing parentheses in O(N) time and O(1) space.

