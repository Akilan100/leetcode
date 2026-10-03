/**
 * Problem   : 32. Longest Valid Parentheses
 * Difficulty: Hard
 * Link      : https://leetcode.com/problems/longest-valid-parentheses/
 * Tags      : String, Dynamic Programming, Stack
 *
 * Time Complexity : O(N)
 * Space Complexity: O(1)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-09-30
 */

class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = 0, maxLen = 0;
        int n = s.length();
        
        // Left to right pass
        for (int i = 0; i < n; ++i) {
            if (s[i] == '(') left++;
            else right++;
            
            if (left == right) {
                maxLen = max(maxLen, 2 * right);
            } else if (right > left) {
                left = right = 0;
            }
        }
        
        // Right to left pass
        left = right = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == '(') left++;
            else right++;
            
            if (left == right) {
                maxLen = max(maxLen, 2 * left);
            } else if (left > right) {
                left = right = 0;
            }
        }
        
        return maxLen;
    }
};
