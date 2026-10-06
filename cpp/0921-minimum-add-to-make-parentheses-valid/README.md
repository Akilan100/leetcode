# [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

**Difficulty:** `Medium` | **Tags:** `String`, `Stack`, `Greedy`, `Bracket Sequences` | **Date Solved:** `2026-10-06`

---

## Problem Statement

A parentheses string is valid if and only if:

	* It is the empty string,

	* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or

	* It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

	* For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(**(**)))"` or a closing parenthesis to be `"())**)**)"`.

Return *the minimum number of moves required to make *`s`* valid*.

 

Example 1:**

```text

**Input:** s = "())"
**Output:** 1

```

Example 2:**

```text

**Input:** s = "((("
**Output:** 3

```

 

**Constraints:**

	* `1 <= s.length <= 1000`

	* `s[i]` is either `'('` or `')'`.

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

