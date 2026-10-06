/**
 * Problem   : 921. Minimum Add to Make Parentheses Valid
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
 * Tags      : String, Stack, Greedy, Bracket Sequences
 *
 * Time Complexity : O(N)
 * Space Complexity: O(1)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-10-06
 */

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
