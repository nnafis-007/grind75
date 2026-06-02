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

a = [1,2,3,4]
a = productExceptSelf(a)
print(a)