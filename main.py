def calculate():
    st = input()
    nums = []
    i = 0
    while i < len(st):
        nums.append(st[i])
        i += 1
    i = 0
    while i < len(nums):
        if nums[i] == '*':
            nums[i] = int(nums[i - 1]) * int(nums[i + 1])
            del nums[i - 1]
            del nums[i]
            i -= 2

        if nums[i] == '/':
            if nums[i + 1] == '0':
                print("error: divide 0")
            nums[i] = int(nums[i - 1]) / int(nums[i + 1])
            del nums[i - 1]
            del nums[i]
            i -= 2
        i += 1
    i = 0
    while i < len(nums):
        if nums[i] == '+':
            nums[i] = int(nums[i - 1]) + int(nums[i + 1])
            del nums[i - 1]
            del nums[i]
            i -= 2

        if nums[i] == '-':
            nums[i] = int(nums[i - 1]) - int(nums[i + 1])
            del nums[i - 1]
            del nums[i]
            i -= 2

        i += 1
    result = nums[0]
    print(result)


if __name__ == "__main__":
    calculate()

