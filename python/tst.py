def maxSumSubarray(nums) -> int:
    maxSum = nums[0]
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j];
            maxSum = max(maxSum,sum)
    return(maxSum)


def main():
    nums = [-2, -5, 6, -2, -3, 1, 5, -6]
    result = maxSumSubarray(nums)
    print("max sum =",result)

# __Launched from the command line__
if __name__ == '__main__':
    main()