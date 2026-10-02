/**
 * Problem   : 22. Generate Parentheses
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/generate-parentheses/
 * Tags      : String, Dynamic Programming, Backtracking, Bracket Sequences
 *
 * Time Complexity : O(4^n / sqrt(n))
 * Space Complexity: O(n)
 * Benchmark       : 0 ms (Beats 67.20%)
 * Date Solved     : 2026-10-02
 */

class Solution {
private:
    void backtrack(vector<string>& result, string& current, int open, int close, int max) {
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }
        if (open < max) {
            current.push_back('(');
            backtrack(result, current, open + 1, close, max);
            current.pop_back();
        }
        if (close < open) {
            current.push_back(')');
            backtrack(result, current, open, close + 1, max);
            current.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current = "";
        backtrack(result, current, 0, 0, n);
        return result;
    }
};
