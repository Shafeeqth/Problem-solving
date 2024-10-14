class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> symbols = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int i = 0;
        int result = 0;
        while( i < s.length()) {
            if(i < s.length() -1 && symbols[s[i]]<symbols[s[i+1]]) {
                result += symbols[s[i+1]] - symbols[s[i]];
                i += 2;
            } else {
                result += symbols[s[i]];
                i++;
            }
        }
        return result;

        
    }
};