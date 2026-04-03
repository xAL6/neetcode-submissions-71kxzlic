class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        max_count = 0
        len_arr = len(nums)
        for i in range(len_arr):
            if nums[i] == 1:
                temp += 1
            if i+1 == len_arr or nums[i+1] == 0:
                if temp > max_count:
                    max_count = temp
                temp = 0
        return max_count
            
                

        