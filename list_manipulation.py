"""The purpose of this code is to take a list of int and see if which two int's will equal a certain target int"""



def twosum(nums: list[int], target: int) -> list[int]:
        # As a means to simplify the soloution, if there are only 2 items in a list in this case, they will have to be the answer"
        if len(nums) == 2:
            return [0, 1]

#The logic I am using is to start by subtracting one of the int from the list from the target, then check if that sum will equal another value in the list
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
