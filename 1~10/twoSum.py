# 1.两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found=False
        result=[]
        for i in range( len(nums) ):
            for j in range( i+1, len(nums) ):
                if nums[i]+nums[j]==target:
                    result=[i,j]
                    found=True
                    break
            if found:
                break

        return result