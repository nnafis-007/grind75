def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    newStart, newEnd = newInterval
    # print(f"newS : {newStart} | newE : {newEnd}")

    ans = []

    insert_idx = -1
    for i in range(len(intervals)):
        s, e = intervals[i]
        if s > newStart:
            insert_idx = i
            break
        ans.append(intervals[i])

    # at last interval    
    if insert_idx == -1:
        insert_idx = len(intervals)

    # Start - Case 1 : No merge -> insert_idx end is smaller than newStart
    if insert_idx == 0 or intervals[insert_idx - 1][1] < newStart:
        ans.append([newStart,-1]) # dummy -1
    # Start - Case 2 : Merge -> Find the end

    # End - Case 1 -> No merge -> newEnd is smaller than next start
    if insert_idx < len(intervals) and newEnd < intervals[insert_idx][0]:
        if insert_idx > 0 and intervals[insert_idx-1][1] > newEnd:
            newEnd = intervals[insert_idx-1][1]
        ans[len(ans)-1][1] = newEnd
        while insert_idx < len(intervals):
            ans.append(intervals[insert_idx])
            insert_idx += 1
        return ans

    # End - Case 2 -> merge ends
    while insert_idx < len(intervals) and intervals[insert_idx][0] <= newEnd:
        insert_idx += 1
    
    insert_idx -= 1
    newEnd = max(newEnd, intervals[insert_idx][1])
    ans[len(ans)-1][1] = newEnd

    insert_idx += 1
    while insert_idx < len(intervals):
        ans.append(intervals[insert_idx])
        insert_idx += 1

    return ans

# ---------------------------------


ans = insert([[0,5],[8,9]], [3,4])
print(ans)