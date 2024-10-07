class Solution {
public:
    int minLength(string s) {
        stack<char> stack;

        for (auto chr : s) {
            if (!stack.empty() && (chr == 'B' && stack.top() == 'A') ||
                !stack.empty() && chr == 'D' && stack.top() == 'C') {
                stack.pop();
            } else {
                stack.push(chr);
            }
        }
        return stack.size();
    }
};