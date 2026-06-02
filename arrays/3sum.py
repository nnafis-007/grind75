def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    N = len(nums)
    ans = []

    i = 0
    while i < N:
        j = i+1
        k = N-1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else: # MATCH found
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        i += 1
        while i < N and nums[i-1] == nums[i]:
            i += 1

    return ans

# take input
# nums = list(map(int, input("Enter the numbers separated by space: ").split()))
nums = [-2,0,1,1,2]
result = threeSum(nums)
print("Unique triplets that sum to zero:")
for triplet in result:
    print(triplet)


