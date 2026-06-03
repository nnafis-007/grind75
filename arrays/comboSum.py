ans = []

def comboSumRec(candidates : list[int], target:int, currAns:list[int], startIdx:int):
    print(f"call for {candidates[startIdx:]} | target = {target} | currAns : {currAns}")
    if target == 0:
        print(f"------ appending {currAns} ---------")
        ans.append(currAns[:])
        return
    
    for i in range(startIdx, len(candidates)):
        num = candidates[i]
        if target - num < 0:
            continue
        currAns.append(num)
        comboSumRec(candidates, target - num, currAns, i)
        currAns.pop()
    # if currAns:



def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # candidates.sort()
    comboSumRec(candidates, target, [], 0)
    return ans

candi = [2,3,5]
combo = combinationSum(candi, 8)
print(combo)
    