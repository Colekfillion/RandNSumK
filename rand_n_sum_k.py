import random


def rand_n_sum_k(n, k):
    x_arr = []
    for xyz in range(n-1):
        num = None
        while True:
            if num is None or num in x_arr:
                num = random.randint(1, k + n-1)
            else:
                x_arr.append(num)
                break
    x_arr.sort()

    rand_num_arr = []
    for index in range(n):
        if index == 0:
            rand_num_arr.append(x_arr[index] - 1)
        elif index == n-1:
            rand_num_arr.append(k + n - 1 - x_arr[index - 1])
        else:
            rand_num_arr.append(x_arr[index] - x_arr[index-1] - 1)

    return rand_num_arr
