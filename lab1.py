import random
import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name')
    parser.add_argument('--task')
    return parser


def word_translate(word):
    for lit in word:
        if not lit.isalpha():
            word = word[:word.find(lit)] + word[word.find(lit) + 1:]
    return word


def quick_sort(nums, first_index, last_index):
    if first_index >= last_index:
        return
    left_index, right_index = first_index, last_index
    pivot = random.choice(nums)

    while left_index <= right_index:
        while nums[left_index] < pivot:
            left_index += 1
        while nums[right_index] > pivot:
            right_index -= 1
        if left_index <= right_index:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index, right_index = left_index + 1, right_index - 1
    quick_sort(nums, first_index, right_index)
    quick_sort(nums, left_index, last_index)


def merge(left, right):
    sorted_list = []
    left_index = right_index = 0
    left_length, right_length = len(left), len(right)

    for i in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1
        elif left_index == left_length:
            sorted_list.append(right[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted_list.append(left[left_index])
            left_index += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
file = format(namespace.name)
task_numb = int(format(namespace.task))


if task_numb == 1 or task_numb == 2:
    d = {}
    with open(file) as inf:
        while True:
            line = inf.readline().lower().split()
            if len(line) == 0:
                break
            for current_word in line:
                current_word = word_translate(current_word)
                if current_word in d.keys():
                    d[current_word] += 1
                else:
                    d[current_word] = 1
    if task_numb == 1:
        for key, value in d.items():
            print(key, value)
    else:
        list_index = [0 for i in range(0, 10)]
        list_words = []
        for key, value in d.items():
            if value > min(list_index):
                list_index[list_index.index(min(list_index))] = value
                list_words.append(key)
        print(*list_words)

elif task_numb == 3:
    with open(file) as inf_numbs:
        numbs = [int(i) for i in inf_numbs.readline().split()]
    quick_sort(numbs, 0, len(numbs) - 1)
    print(*numbs)

elif task_numb == 4:
    with open(file) as inf_numbs:
        numbs = [int(i) for i in inf_numbs.readline().split()]
    numbs = merge_sort(numbs)
    print(*numbs)

elif task_numb == 5:
    with open(file) as inf_count:
        count = int(inf_count.readline())
    for fib in fibonacci(count):
        print(fib, end=" ")
