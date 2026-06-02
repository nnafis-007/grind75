def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    N = len(nums)
    prefix = [1]
    suffix = [1]*N
    for i in range(1, N):
        prefix.append(prefix[i-1] * nums[i-1])
    
    for i in range(N-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    print("prefix products : ", prefix)
    print("suffix products : ", suffix)
    
    for i in range(N):
        suffix[i] = suffix[i] * prefix[i]
    return suffix

# SC -> O(1) [excluding answer array]
def prodExceptSelfOptimized(nums):
    N = len(nums)
    ans_array = [1]
    temp = 1

    # Create Prefix Array
    for i in range(1, N):
        ans_array.append(nums[i-1] * ans_array[i-1])
    
    for i in range(N-2, -1, -1):
        temp = temp * nums[i+1] # calc suffix product
        ans_array[i] = temp * ans_array[i] # ans = prefix * suffix
    
    return ans_array

a = [1,2,3,4]
a = prodExceptSelfOptimized(a)
print(a)