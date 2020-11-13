def runningSum(nums):
    emp_list = []
    for i, j in enumerate(nums):
        emp_list.append(sum(nums[:i+1]))
    return emp_list

nums = [1,2,3,4]
print(runningSum(nums))
nums = [1,1,1,1,1,1]
print(runningSum(nums))
