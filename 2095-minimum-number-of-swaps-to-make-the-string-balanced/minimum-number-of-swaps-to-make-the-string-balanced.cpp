class Solution {
public:
    int minSwaps(string s) {
        int imperfect = 0;
        for (const auto ch : s) {
            if (ch == ']') {
                if (imperfect == 0) {
                    imperfect++;
                } else {
                    imperfect--;
                }
            } else {
                imperfect++;
            }
        }
        return (imperfect + 1) / 2;
    }
};