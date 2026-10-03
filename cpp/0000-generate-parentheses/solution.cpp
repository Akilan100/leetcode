/**
 * Problem   : 0. generate-parentheses
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/generate-parentheses/
 * Tags      : 
 *
 * Time Complexity : O(4^N / sqrt(N))
 * Space Complexity: O(N)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-10-03
 */

class Solution {
private:
    void backtrack(int open, int close, int n, string& cur, vector<string>& res) {
        if (cur.length() == 2 * n) {
            res.push_back(cur);
            return;
        }
        if (open < n) {
            cur.push_back('(');
            backtrack(open + 1, close, n, cur, res);
            cur.pop_back();
        }
        if (close < open) {
            cur.push_back(')');
            backtrack(open, close + 1, n, cur, res);
            cur.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string cur = "";
        backtrack(0, 0, n, cur, res);
        return res;
    }
};
