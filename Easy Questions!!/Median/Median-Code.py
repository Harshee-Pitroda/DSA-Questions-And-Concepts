def median(nums):
    if nums:
        sorted_nums = sorted(nums)
        if len(sorted_nums)%2==0:
            num2 = sorted_nums[int(len(sorted_nums)/2)]
            num1 = sorted_nums[int(len(sorted_nums)/2) - 1]
            return (num1+num2)/2
        else:
            return sorted_nums[len(sorted_nums)//2]
    else:
        return None

print(median([5, 1 , 2 ,3]))