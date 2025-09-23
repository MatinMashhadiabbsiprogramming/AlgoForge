# 217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i-1]:
                 return True
                 break
        
        return False
# test1 
listNum=[1, 2, 2, 3, 4, 5,5]
obj=Solution()
obj1=obj.containsDuplicate(listNum)
print(obj1)
# test2 
listNum2=[1, 2, 3, 4, 5]
obj2=Solution()
obj2=obj.containsDuplicate(listNum2)
print(obj2)