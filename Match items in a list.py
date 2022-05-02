



def twosum(nums: list[int], target: int) -> list[int]:
        if len(nums) == 2:
            return [0, 1]

        for index in range(0, len(nums) - 1):
            try:
                x = target - nums[index]
                newArr = nums.copy()
                newArr.pop(index)
                secondIndex = newArr.index(x)
                return [index, secondIndex + 1]
            except ValueError:
                continue


print(twosum(nums= [7,11,3,5,6,8], target= 10))
