/**
 * Problem   : 96. Unique Binary Search Trees
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/unique-binary-search-trees/
 * Tags      : Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree
 *
 * Time Complexity : O(N)
 * Space Complexity: O(1)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-09-30
 */

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
