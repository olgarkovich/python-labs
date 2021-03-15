import random
import os


def merge(left, right):
    sorted_list = []
    left_index = right_index = 0
    left_length, right_length = len(left), len(right)

    for _ in range(left_length + right_length):
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


def merge_files(current_file, file_length, current_list, result_file):
    file_index = list_index = 0
    list_length = len(current_list)
    current_file.seek(0)
    result_file.seek(0)
    current_file_numb = current_file.readline()
    for _ in range(file_length + list_length):
        if file_index < file_length and list_index < list_length:
            try:
                current_file_numb = int(current_file_numb)
                if current_file_numb <= current_list[list_index]:
                    result_file.write('{}\n'.format(current_file_numb))
                    current_file_numb = current_file.readline()
                    file_index += 1
                else:
                    result_file.write('{}\n'.format(current_list[list_index]))
                    list_index += 1
            except ValueError:
                if file_index < file_length:
                    current_file_numb = current_file.readline()
                print("Error")
        elif file_index == file_length:
            result_file.write('{}\n'.format(current_list[list_index]))
            list_index += 1
        elif list_index == list_length:
            if isinstance(current_file_numb, int):
                result_file.write('{}\n'.format(current_file_numb))
            else:
                result_file.write('{}'.format(current_file_numb))
            current_file_numb = current_file.readline()
            file_index += 1


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def start():
    count = int(input("Enter quantity of numb "))
    part = 200000

    steps = count // part if count % part == 0 else count // part + 1
    with open("numbs_2.txt", 'w') as out_file:
        out_file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(count - 1))
        out_file.writelines('{}'.format(random.randint(-1000, 1000)))
    lists = []
    with open("numbs_2.txt") as input_file:
        for step in range(steps):
            my_list = []
            for _ in range(part):
                str = input_file.readline()
                if str[:-1] != '':
                    my_list.append(int(str[:-1]))
            my_list = merge_sort(my_list)
            with open('numbs_step_{}.txt'.format(step), "w") as out_file:
                for i in my_list:
                    out_file.writelines('{}\n'.format(i))
            lists = merge(lists, my_list)
    path = os.path.join('numbs_2.txt')
    os.remove('numbs_2.txt')
    step = 0
    while step != steps - 1:
        list_numb = []
        with open("numbs_step_{}.txt".format(step + 1), 'r') as out_fst_file:
            list_numb = [int(i) for i in out_fst_file.readlines()]
        with open("numbs_step_{}.txt".format(step), 'r') as out_snd_file:
            with open("numbs_step_{}.txt".format(step + 1), 'w') as in_file:
                merge_files(out_snd_file, part * (step + 1), list_numb, in_file)
        path = os.path.join("numbs_step_{}.txt".format(step))
        os.remove(path)
        step += 1
        print(step)
    os.rename("numbs_step_{}.txt".format(step), "numbs_2.txt")
