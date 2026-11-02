class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        olMap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in olMap:
                return [olMap[diff], i]
            olMap[n] = i
        return
           