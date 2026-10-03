/**
 * Problem   : 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
 * Tags      : String, Stack, Bracket Sequences
 *
 * Time Complexity : O(N)
 * Space Complexity: O(1)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-10-03
 */

class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        vector<int> ans(seq.size());
        int depth = 0;
        for (int i = 0; i < (int)seq.size(); ++i) {
            if (seq[i] == '(') {
                ans[i] = depth % 2;
                depth++;
            } else {
                depth--;
                ans[i] = depth % 2;
            }
        }
        return ans;
    }
};
