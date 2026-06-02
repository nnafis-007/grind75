
ans = []
def gen_all_subsets(arr : list[int], curr_subset : list[int], idx : int):
    if idx >= len(arr):
        print(f"    appending {curr_subset} | index : {idx}")
        ans.append(curr_subset[:])
        return

    curr_subset.append(arr[idx])
    curr1 : list[int] = curr_subset 
    print("Recursive call for ", curr1)
    gen_all_subsets(arr, curr1, idx+1)
    curr1.pop()
    print("popped & Recursive call for ", curr1)
    gen_all_subsets(arr, curr1, idx+1)

a = [1,2,3]
curr_ss = []
gen_all_subsets(a, curr_ss, 0)

print(ans)