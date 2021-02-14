class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> res;
        vector<int> lastIdxs(26,0);
        
        for(int i = 0; i < S.size(); i++) {
            lastIdxs[S[i] - 'a'] =  i;
        }
        
        int i = 0;
        while(i < S.size()) {
            int end = lastIdxs[S[i] - 'a'];
            int j = i;
            while(j != end) {
                end = max(end, lastIdxs[S[j] - 'a']);
                j++;
            }
            
            res.push_back(j - i + 1);
            i = j + 1;
        }
        
        return res;
        
    }
};
