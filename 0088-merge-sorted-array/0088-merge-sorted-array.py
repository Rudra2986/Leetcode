class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    
        insert_ptr = 0

        for i in range(m,len(nums1)):
            nums1.pop(i)
            nums1.insert(i,nums2[insert_ptr])
            insert_ptr+=1
            
        nums1.sort()