/**
 * Problem   : 20. Valid Parentheses
 * Difficulty: Easy
 * Link      : https://leetcode.com/problems/valid-parentheses/
 * Tags      : String, Stack, Bracket Sequences
 *
 * Time Complexity : O(N)
 * Space Complexity: O(N)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-10-01
 */

class Solution {
public:
    bool isValid(string s) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        vector<char> st;
        st.reserve(s.size());
        
        for (char c : s) {
            if (c == '(') st.push_back(')');
            else if (c == '{') st.push_back('}');
            else if (c == '[') st.push_back(']');
            else {
                if (st.empty() || st.back() != c) return false;
                st.pop_back();
            }
        }
        return st.empty();
    }
};
