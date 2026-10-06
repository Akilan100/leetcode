/**
 * Problem   : 0. minimum-add-to-make-parentheses-valid
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
 * Tags      : 
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
