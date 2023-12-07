class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = nums1.size()-1;
        int p1 = m-1;
        int p2 = n-1;

        while(true){
            if(p1 < 0 || p2 < 0) break;
            if(nums1[p1] <= nums2[p2]){
                nums1[i] = nums2[p2];
                i--;
                p2--;
            }else if(nums1[p1] > nums2[p2]){
                int temp = nums1[p1];
                nums1[p1] = nums1[i];
                nums1[i] = temp;
                ptr1--;
                i--;
            }
        }
        while(p2 >= 0){
            nums1[i] = nums2[p2];
            i--;
            p2--;
        }
    }
};sdasd:wq

