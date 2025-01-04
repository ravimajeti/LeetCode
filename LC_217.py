class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    
    def containsDuplicate_usingSets(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) 

if __name__ == "__main__":
    nums = [1,2,3,1]
    solution = Solution()
    print(solution.containsDuplicate(nums))
    print(solution.containsDuplicate_usingSets(nums))
    nums = [1,2,3,4]
    print(solution.containsDuplicate(nums))
    print(solution.containsDuplicate_usingSets(nums))
