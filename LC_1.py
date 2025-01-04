class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tracker_dict = {}
        for index, num in enumerate(nums):
            other_num = target - num
            if other_num in tracker_dict:
                return [index, tracker_dict[other_num]]
            tracker_dict[num] = index
        return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))