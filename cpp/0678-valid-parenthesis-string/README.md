# [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)

**Difficulty:** `Medium` | **Tags:** `String`, `Dynamic Programming`, `Stack`, `Greedy` | **Date Solved:** `2026-10-04`

---

## Problem Statement



---

## Solution (C++)

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(1)`
* **Performance:** `2 ms` (Beats `13.10%`)

```cpp
class Solution {
public:
    bool checkValidString(string s) {
        int minOpen = 0, maxOpen = 0;
        for (char c : s) {
            if (c == '(') {
                minOpen++;
                maxOpen++;
            } else if (c == ')') {
                minOpen--;
                maxOpen--;
            } else { // '*'
                minOpen--;
                maxOpen++;
            }
            if (maxOpen < 0) return false;
            minOpen = max(minOpen, 0);
        }
        return minOpen == 0;
    }
};
```

### Key Intuition
**Greedy Range-Tracking Algorithm**

Track the **range of possible open-parenthesis counts** `[minOpen, maxOpen]`:
- `'('` → both increment (`minOpen++`, `maxOpen++`)
- `')'` → both decrement (`minOpen--`, `maxOpen--`)
- `'*'` → `minOpen--` (treat as `)`), `maxOpen++` (treat as `(`)

**Invariants:**
1. If `maxOpen < 0`: return `false` (excess closing parentheses)
2. `minOpen = max(minOpen, 0)`: can never have negative unclosed open parentheses
3. Return `minOpen == 0` at termination

