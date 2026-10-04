# [0. valid-parenthesis-string](https://leetcode.com/problems/valid-parenthesis-string/)

**Difficulty:** `Medium` | **Tags:** `Algorithms` | **Date Solved:** `2026-10-04`

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
    bool checkValidString(string s) {
        // Greedy: maintain [minOpen, maxOpen] range of valid open-paren counts
        // '(' -> both ++, ')' -> both --, '*' -> minOpen-- maxOpen++
        // If maxOpen < 0: impossible (excess ')')
        // Valid iff minOpen == 0 at end
        int minOpen = 0, maxOpen = 0;
        for (char c : s) {
            if (c == '(') {
                minOpen++;
                maxOpen++;
            } else if (c == ')') {
                minOpen--;
                maxOpen--;
            } else { // '*'
                minOpen--;   // treat as ')'
                maxOpen++;   // treat as '('
            }
            if (maxOpen < 0) return false;   // too many ')'
            minOpen = max(minOpen, 0);        // floor at 0
        }
        return minOpen == 0;
    }
};
```

### Key Intuition
**Greedy Range-Tracking** — O(N) time, O(1) space

Track the **range of possible open-parenthesis counts** as a window `[minOpen, maxOpen]`:
- `'('` → both bounds +1 (must open)
- `')'` → both bounds -1 (must close)
- `'*'` → `minOpen-1`, `maxOpen+1` (wildcard: can be `(`, `)`, or empty)

**Key Invariants:**
1. If `maxOpen < 0` at any point → impossible (too many unmatched `)`)
2. Clamp `minOpen = max(minOpen, 0)` (open count can't go negative)
3. Valid iff `minOpen == 0` at the end (all opens can be matched)

This collapses the O(N²) DP state space into a single O(1) interval — no stack, no memoization table.

