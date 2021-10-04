class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=nums1+nums2
        lst=sorted(lst)
        if len(lst)==1:
            return lst[0]
        elif len(lst)%2==1:
            return(lst[len(lst)//2])
        else:
            m=lst[(len(lst)//2)-1]+lst[len(lst)//2]
            return m/2
        
