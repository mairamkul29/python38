def rm_element(nums, val):
    k = []
    for num in nums:
        if num != val:
            k.append(num)
    
    return len(k)

print(rm_element(nums=[3,2,2,3], val=3))