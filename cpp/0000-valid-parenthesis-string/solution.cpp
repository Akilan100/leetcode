/**
 * Problem   : 0. valid-parenthesis-string
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/valid-parenthesis-string/
 * Tags      : 
 *
 * Time Complexity : O(N)
 * Space Complexity: O(1)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-10-04
 */

class Solution {
public:
    bool checkValidString(string s) {
        // Greedy: maintain [minOpen, maxOpen] range of valid open-paren counts
        // '(' -> both ++, ')' -> both --, '*' -> minOpen-- maxOpen++
        // If maxOpen < 0: impossible (excess ')')
        // Valid iff minOpen == 0 at end
        int minOpen = 0, maxOpen = 0;
        for (char c : s) {
            if (c == '(') {
                minOpen++;
                maxOpen++;
            } else if (c == ')') {
                minOpen--;
                maxOpen--;
            } else { // '*'
                minOpen--;   // treat as ')'
                maxOpen++;   // treat as '('
            }
            if (maxOpen < 0) return false;   // too many ')'
            minOpen = max(minOpen, 0);        // floor at 0
        }
        return minOpen == 0;
    }
};
