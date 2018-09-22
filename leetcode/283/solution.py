ass Solution(object):
        def moveZeroes(self, nums):
            n=count(0)
            for i in range(n):
                nums.remove(0)
            nums.extend([0]*n)
