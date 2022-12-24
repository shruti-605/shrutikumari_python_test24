from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    index_map = {}
    for i, n in enumerate(nums):
        difference = target - n
        if difference in index_map:
            result.append(i)
            result.append(index_map[difference])
            break
        else:
            index_map[n] = i
    return result
print(twoSum([3,3],6))