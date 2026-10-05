# [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

**Difficulty:** `Medium` | **Tags:** `String`, `Stack`, `Bracket Sequences` | **Date Solved:** `2026-10-05`

---

## Problem Statement

Given a balanced parentheses string `s`, return *the **score** of the string*.

The score of a balanced parentheses string is based on the following rule:
* `"()"` has score `1`.
* `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
* `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

### Example 1:
```text
Input: s = "()"
Output: 1
```

### Example 2:
```text
Input: s = "(())"
Output: 2
```

### Example 3:
```text
Input: s = "()()"
Output: 2
```

### Constraints:
* `2 <= s.length <= 50`
* `s` consists of only `'('` and `')'`.
* `s` is a balanced parentheses string.

---

## Solutions

### 1. C++ (Primary)
* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(1)`
* **Performance:** `0 ms` (Beats `100.00%`), `7.90 MB` (Beats `95.79%`)

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int scoreOfParentheses(string s) {
        int score = 0;
        int depth = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                depth++;
            } else {
                depth--;
                if (s[i - 1] == '(') {
                    score += (1 << depth);
                }
            }
        }
        return score;
    }
};
```

### 2. Java
* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(1)`

```java
class Solution {
    public int scoreOfParentheses(String s) {
        int score = 0, depth = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                depth++;
            } else {
                depth--;
                if (s.charAt(i - 1) == '(') {
                    score += (1 << depth);
                }
            }
        }
        return score;
    }
}
```

### 3. Python 3
* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(1)`

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += (1 << depth)
        return score
```

---

## Detailed Explanation & Key Intuition

### Counting Cores / Tree Leaves (Bit-Shift Approach)
Every balanced parentheses string can be visualized as an expression tree where the fundamental units with value are the primitive pairs `()`. 
- Each primitive pair `()` represents a base score of `1`.
- When wrapped inside outer parentheses, its value doubles for every enclosing level: a pair at depth $d$ contributes $2^d$ to the total sum.
- Because multiplication distributes over addition ($2 \times (A + B) = 2A + 2B$), we only need to identify every immediately adjacent `"()"` substring, calculate its contribution as $2^{\text{depth}}$ (using bit shift `1 << depth`), and sum them up.

### Algorithm Steps:
1. Maintain `depth = 0` and `score = 0`.
2. Iterate through string `s`:
   - If `s[i] == '('`, increment `depth`.
   - If `s[i] == ')'`, decrement `depth`. If the immediately preceding character was `'('` (i.e. `s[i - 1] == '('`), add `1 << depth` ($2^{\text{depth}}$) to `score`.
3. Return `score`.

---

## ⏱️ Complexity Analysis
* **Time Complexity:** `O(N)` — Single linear pass across the string of length $N$.
* **Space Complexity:** `O(1)` — Only constant extra space used for tracking current depth and total score.
