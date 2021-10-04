class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices=[]
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
if __name__ == '__main__':
    num=[1,2,3,4,5,6]            
    objec=Solution()  
    print(objec.twoSum(num,5))                    
 
