 #        remove duplicates from sorted array(medium)

 
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l=0
    n=len(nums)
    hash={}
    for i in range(n):
        if nums[i] not in hash:
            hash[nums[i]]=1
        elif(nums[i] in hash):
            hash[nums[i]]=2
    # print(hash)
    nums=[]
    for x in hash:
        nums.extend([x]*hash[x])
    return nums
print(removeDuplicates([1,1,1,2,2,2,3,4,5,6,7,8,8]))

