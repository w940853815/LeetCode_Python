# -*- coding: utf-8 -*-
# coding=utf-8
__author__ = 'ruidong.wang@tsingdata.com'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target == nums[i] + nums[j]:
                    if i==j:
                        break
                    list.append(i)
                    list.append(j)
                    return list

if __name__ == '__main__':
    nums=[3,2,4]
    target=6
    s=Solution()
    print s.twoSum(nums,target)