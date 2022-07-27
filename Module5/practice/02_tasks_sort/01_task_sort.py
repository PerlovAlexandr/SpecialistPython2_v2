import random

def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        j += 1
        for i in range(len(nums) - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = random.randint(-100,100)
sum_num = 0
for number in numbers:
    if number > a:
        sum_num +=number

print(a)
print(sum_num)
