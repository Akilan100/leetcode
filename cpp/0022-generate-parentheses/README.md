# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

**Difficulty:** `Medium` | **Tags:** `String`, `Dynamic Programming`, `Backtracking`, `Bracket Sequences` | **Date Solved:** `2026-10-02`

---

## Problem Statement

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

 

Example 1:**

```text
**Input:** n = 3
**Output:** ["((()))","(()())","(())()","()(())","()()()"]

```

Example 2:**

```text
**Input:** n = 1
**Output:** ["()"]

```

 

**Constraints:**

	* `1 <= n <= 8`

---

## Solution (C++)

* **Time Complexity:** `O(4^n / sqrt(n))`
* **Space Complexity:** `O(n)`
* **Performance:** `0 ms` (Beats `67.20%`)

```cpp
class Solution {
private:
    void backtrack(vector<string>& result, string& current, int open, int close, int max) {
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }
        if (open < max) {
            current.push_back('(');
            backtrack(result, current, open + 1, close, max);
            current.pop_back();
        }
        if (close < open) {
            current.push_back(')');
            backtrack(result, current, open, close + 1, max);
            current.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current = "";
        backtrack(result, current, 0, 0, n);
        return result;
    }
};
```

### Key Intuition
Classic backtracking: at each position choose to add '(' if open < n, or add ')' if close < open. Terminate when string length == 2*n.

