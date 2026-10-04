/**
 * Problem   : 678. Valid Parenthesis String
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/valid-parenthesis-string/
 * Tags      : String, Dynamic Programming, Stack, Greedy
 *
 * Time Complexity : O(N)
 * Space Complexity: O(1)
 * Benchmark       : 2 ms (Beats 13.10%)
 * Date Solved     : 2026-10-04
 */

class Solution {
public:
    bool checkValidString(string s) {
        int minOpen = 0, maxOpen = 0;
        for (char c : s) {
            if (c == '(') {
                minOpen++;
                maxOpen++;
            } else if (c == ')') {
                minOpen--;
                maxOpen--;
            } else { // '*'
                minOpen--;
                maxOpen++;
            }
            if (maxOpen < 0) return false;
            minOpen = max(minOpen, 0);
        }
        return minOpen == 0;
    }
};
