nums=[60,71,49,11,82,49,3,66]
step=int(len(nums)/2)

while step>0:
    print("step is: %d" % step)
    for i in range(step, len(nums)):
        while i>=step and nums[i-step]>nums[i]:
            print("i is: %d" % i)
            nums[i],nums[i-step]=nums[i-step],nums[i]
            print(nums)
            i-=step
    step=int(step/2)
print(nums)