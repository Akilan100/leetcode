# [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)

**Difficulty:** `Medium` | **Tags:** `Math`, `Dynamic Programming`, `Tree`, `Binary Search Tree`, `Binary Tree` | **Date Solved:** `2026-09-30`

---

## Problem Statement

Given an integer `n`, return *the number of structurally unique **BST'**s (binary search trees) which has exactly *`n`* nodes of unique values from* `1` *to* `n`.

 

Example 1:**

```text

**Input:** n = 3
**Output:** 5

```

Example 2:**

```text

**Input:** n = 1
**Output:** 1

```

 

**Constraints:**

	* `1 <= n <= 19`

---

## Solution (C++)

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(1)`
* **Performance:** `0 ms` (Beats `100.00%`)

```cpp
class Solution {
public:
    int numTrees(int n) {
        long long c = 1;
        for (int i = 0; i < n; ++i) {
            c = c * 2 * (2 * i + 1) / (i + 2);
        }
        return (int)c;
    }
};
```

### Key Intuition
Computed via closed-form Catalan numbers recursion: C_n = C_{n-1} * 2*(2n-1)/(n+1).

