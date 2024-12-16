class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        std::set<int> banned_set;
        std::copy_if(banned.begin(), banned.end(),
                     std::inserter(banned_set, banned_set.end()),
                     [maxSum](int x) { return x <= maxSum; });
        int counter = 0;
        for(int i = 1; i <= n; i++) {
            if(!banned_set.contains(i)) {
                if(maxSum - i >= 0) {
                    maxSum -= i;
                    ++counter;
                }
            }
        }

        return counter;


        for(auto elem : banned_set) {
            cout << elem << ' ';
        }
        return 0;
    }
};