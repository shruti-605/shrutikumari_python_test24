class Solution:
    def maxProductDifference(nums):

        return (sorted(nums)[-1]*sorted(nums)[-2])-(sorted(nums)[0]*sorted(nums)[1])
    print(maxProductDifference([5,6,2,7,4]))