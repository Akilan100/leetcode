# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

**Difficulty:** `Easy` | **Tags:** `String`, `Stack`, `Bracket Sequences` | **Date Solved:** `2026-10-01`

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	* Open brackets must be closed by the same type of brackets.

	* Open brackets must be closed in the correct order.

	* Every close bracket has a corresponding open bracket of the same type.

 

Example 1:**

**Input:** s = "()"

**Output:** true

Example 2:**

**Input:** s = "()[]{}"

**Output:** true

Example 3:**

**Input:** s = "(]"

**Output:** false

Example 4:**

**Input:** s = "([])"

**Output:** true

Example 5:**

**Input:** s = "([)]"

**Output:** false

 

**Constraints:**

	* `1 <= s.length <= 104`

	* `s` consists of parentheses only `'()[]{}'`.

---

## Solution (C++)

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(N)`
* **Performance:** `0 ms` (Beats `100.00%`)

```cpp
class Solution {
public:
    bool isValid(string s) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        vector<char> st;
        st.reserve(s.size());
        
        for (char c : s) {
            if (c == '(') st.push_back(')');
            else if (c == '{') st.push_back('}');
            else if (c == '[') st.push_back(']');
            else {
                if (st.empty() || st.back() != c) return false;
                st.pop_back();
            }
        }
        return st.empty();
    }
};
```

### Key Intuition
Stack-based character matching using vector buffer and I/O fast synchronization.

