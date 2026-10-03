# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

**Difficulty:** `Hard` | **Tags:** `String`, `Dynamic Programming`, `Stack`, `Bracket Sequences` | **Date Solved:** `2026-10-03`

---

## Problem Statement

Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses **substring*.

 

Example 1:**

```text

**Input:** s = "(()"
**Output:** 2
**Explanation:** The longest valid parentheses substring is "()".

```

Example 2:**

```text

**Input:** s = ")()())"
**Output:** 4
**Explanation:** The longest valid parentheses substring is "()()".

```

Example 3:**

```text

**Input:** s = ""
**Output:** 0

```

 

**Constraints:**

	* `0 <= s.length <= 3 * 104`

	* `s[i]` is `'('`, or `')'`.

---

## Solution (C++)

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(N)`
* **Performance:** `0 ms` (Beats `100.00%`)

```cpp
/**
 * Problem   : 32. Longest Valid Parentheses
 * Difficulty: Hard
 * Link      : https://leetcode.com/problems/longest-valid-parentheses/
 * Tags      : String, Dynamic Programming, Stack, Bracket Sequences
 *
 * Approach  :
 * Use a stack to store the indices of characters. Initialize stack with -1 to serve
 * as a base for valid substring length calculations.
 * Iterate through the string:
 *   - For '(', push its index onto the stack.
 *   - For ')', pop the top index. If the stack is empty after popping, push the current index
 *     as the new base. If not empty, calculate the current valid substring length as 
 *     and update maxLen.
 *
 * Complexity:
 *   Time  : O(N) where N is the length of the string
 *   Space : O(N) for stack storage
 */

#include <string>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLen = 0;
        stack<int> st;
        st.push(-1);
        
        for (int i = 0; i < (int)s.length(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.empty()) {
                    st.push(i);
                } else {
                    maxLen = max(maxLen, i - st.top());
                }
            }
        }
        
        return maxLen;
    }
};
```

### Key Intuition
Stack-based index tracking maintaining base boundary at top of stack.

