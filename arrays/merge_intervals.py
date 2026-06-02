def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort()
    N = len(intervals)
    res = []
    res.append(intervals[0])
    res.append(intervals[1])
    i = 1
    j = 1
    while i < N:
        j = len(res) - 1
        cs, ce = res[j-1]
        ns, ne = res[j]
        # Merge if overlap
        if ns <= ce:
            res.pop()
            res.pop()
            res.append([min(cs,ns),max(ce,ne)])
        if i < N-1: 
            res.append(intervals[i+1])
        i += 1
    return res


intervals = [[1,3], [2,6], [8,10], [15,18]]
intervals = merge(intervals)
print(intervals)
