import copy

ans = []

def gen_all_perm(
        arr : list[int], 
        curr_perm : list[int],
        used : list[bool]
    ):
    if len(curr_perm) == len(arr):
        ans.append(curr_perm[:])

    # For each element
    for i in range(len(arr)):
        if used[i]:
            continue

        # No one downstream can use this anymore
        used[i] = True 
        curr_perm.append(arr[i])

        gen_all_perm(arr, curr_perm, used) # Gen all perms by fixing the curr elem
        
        # Before next iteration, free up this curr elem so that it can be used downstream
        used[i] = False  
        curr_perm.pop() 
        

arr = [1,2,3]
used = [False]*len(arr)
gen_all_perm(arr, [], used)
i = 1
for a in ans:
    print(f"{i}. {a}")
    i += 1