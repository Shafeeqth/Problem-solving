class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged_word = "";
        int w1_size = word1.length();
        int w2_size = word2.length();
        int x = 0, y = 0;
        while(x < w1_size && y < w2_size) {
            merged_word += word1[x++];
            merged_word += word2[y++];
        }
        while(x < w1_size) {
            merged_word += word1[x++];
        }
        while(y < w2_size) {
            merged_word += word2[y++];
        }
        return merged_word;

        
    }
};