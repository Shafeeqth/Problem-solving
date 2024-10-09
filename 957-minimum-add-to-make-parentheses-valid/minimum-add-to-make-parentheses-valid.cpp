class Solution {
public:
    int minAddToMakeValid(string s) {
        int imperfect = 0;
        stack<char> stack;

        for (const auto ch : s) {
            if (ch == ')') {
                if (!stack.empty() && stack.top() == '(') {
                    stack.pop();
                } else {
                    stack.push(ch);
                }

            } else {
                stack.push(ch);
            }
        }
        return stack.size();
    }
};