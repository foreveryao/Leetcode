class Solution{
public:
    int removeDuplicates(vector<int>& nums){
        if (nums.size()==0)
        {
            return 0;
        }
        else if (nums.size()==1)
        {
            return 1;
        }
        int number=0;

        for (int i=0;i<nums.size();++i)
        {
            if (nums[i]!=nums[number])
            {
                number++;
                nums[number]=nums[i];
            }
        }
        return number+1;
    }
}
