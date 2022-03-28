from typing import List

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            if target - nums[i] in num_map:
                return [num_map[target - nums[i]], i]
            num_map[nums[i]] = i
        return None


result = Solution().twoSum([2, 7, 11, 15], 9)
assert result == [0, 1], result

result = Solution().twoSum([3, 2, 4], 6)
assert result == [1, 2], result

result = Solution().twoSum([3, 3], 6)
assert result == [0, 1], result

print("All tests passed!")
