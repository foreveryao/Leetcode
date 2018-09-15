ass Solution(object):
        def rotate(self, nums, k):
            nums[:l-k]=reversed(nums[:l-k])
            nums[l-k:]=reversed(nums[l-k:])
            nums[:]=reversed(nums)
