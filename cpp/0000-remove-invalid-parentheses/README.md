# [0. remove-invalid-parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)

**Difficulty:** `Medium` | **Tags:** `Algorithms` | **Date Solved:** `2026-10-07`

---

## Problem Statement



---

## Solution (C++)

* **Time Complexity:** `O(2^N)`
* **Space Complexity:** `O(N)`
* **Performance:** `0 ms` (Beats `100.00%`)

```cpp
class Solution {
public:
    void remove(string s, int last_i, int last_j, const string& par, vector<string>& ans) {
        int count = 0;
        for (int i = last_i; i < s.length(); i++) {
            if (s[i] == par[0]) count++;
            if (s[i] == par[1]) count--;
            if (count >= 0) continue;
            
            // count < 0: we have an extra par[1] to remove
            for (int j = last_j; j <= i; j++) {
                if (s[j] == par[1] && (j == last_j || s[j - 1] != par[1])) {
                    remove(s.substr(0, j) + s.substr(j + 1), i, j, par, ans);
                }
            }
            return;
        }
        
        string rev = s;
        reverse(rev.begin(), rev.end());
        if (par[0] == '(') {
            remove(rev, 0, 0, ")(", ans);
        } else {
            ans.push_back(rev);
        }
    }

    vector<string> removeInvalidParentheses(string s) {
        vector<string> ans;
        remove(s, 0, 0, "()", ans);
        return ans;
    }
};
```

### Key Intuition
Using DFS with bidirectional pruning guarantees minimum removals and strictly unique results without set allocations. We scan left-to-right to remove invalid `')'`. When balanced, we reverse the string and mirror the logic to eliminate invalid `'('`.

