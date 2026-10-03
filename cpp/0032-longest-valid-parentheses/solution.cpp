/**
 * Problem   : 32. Longest Valid Parentheses
 * Difficulty: Hard
 * Link      : https://leetcode.com/problems/longest-valid-parentheses/
 * Tags      : String, Dynamic Programming, Stack, Bracket Sequences
 *
 * Time Complexity : O(N)
 * Space Complexity: O(N)
 * Benchmark       : 0 ms (Beats 100.00%)
 * Date Solved     : 2026-10-03
 */

/**
 * Problem   : 32. Longest Valid Parentheses
 * Difficulty: Hard
 * Link      : https://leetcode.com/problems/longest-valid-parentheses/
 * Tags      : String, Dynamic Programming, Stack, Bracket Sequences
 *
 * Approach  :
 * Use a stack to store the indices of characters. Initialize stack with -1 to serve
 * as a base for valid substring length calculations.
 * Iterate through the string:
 *   - For '(', push its index onto the stack.
 *   - For ')', pop the top index. If the stack is empty after popping, push the current index
 *     as the new base. If not empty, calculate the current valid substring length as 
 *     and update maxLen.
 *
 * Complexity:
 *   Time  : O(N) where N is the length of the string
 *   Space : O(N) for stack storage
 */

#include <string>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLen = 0;
        stack<int> st;
        st.push(-1);
        
        for (int i = 0; i < (int)s.length(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.empty()) {
                    st.push(i);
                } else {
                    maxLen = max(maxLen, i - st.top());
                }
            }
        }
        
        return maxLen;
    }
};
