class Solution {
    public:
    void sortColors(vector<int>& nums) {
        
        int tmp = 0;
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;
        
        while(mid <= high) {
            if(nums[mid] == 0) {
                tmp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = tmp;
                
                low++;
                mid++;
            }
            else if(nums[mid] == 1) {
                mid++;
            }
            else if(nums[mid] == 2) {
                tmp = nums[high];
                nums[high] = nums[mid];
                nums[mid] = tmp;
                
                high--;
            }    
        }
    }
};
