import random
import time
def merge_sort_find_optimal(arr):
    if len(arr) <= 1:
        return arr


    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort_find_optimal(left_half)
    right_half = merge_sort_find_optimal(right_half)


    return save_optimal(left_half, right_half)

def save_optimal(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
            # The left list is eligible and has a smaller x-value
        if left[left_idx][0] <= right[right_idx][0] and left[left_idx][1] >= right[right_idx][1]:
            merged.append(left[left_idx])
            left_idx += 1
            # The right list is eligible and has a smaller x-value
        elif left[left_idx][0] >= right[right_idx][0] and left[left_idx][1] <= right[right_idx][1]:
            merged.append(right[right_idx])
            right_idx += 1
            # The left side is not eligible, skip this element
        elif left[left_idx][0] < right[right_idx][0] and left[left_idx][1] < right[right_idx][1]:
            left_idx+=1
            # The right side is not eligible, skip this element
        elif left[left_idx][0] > right[right_idx][0] and left[left_idx][1] > right[right_idx][1]:
            right_idx+=1
    #Merge the remaining points
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

def generate_random_points(n):
    points = []
    for _ in range(n):
        x = random.randint(0, 100)  # random x in [0,100]
        y = random.randint(0, 100)  # random y in [0,100]
        points.append((x, y))
    return points

n = 10 # number of points
arr = generate_random_points(n)
start_time = time.perf_counter_ns()
sorted_arr = merge_sort_find_optimal(arr)
end_time = time.perf_counter_ns()
elapsed_time_ns = end_time - start_time
print(arr)
print(sorted_arr)
print(f"running time: {elapsed_time_ns} ns")

# show stair
import matplotlib.pyplot as plt

x_arr= [item[0] for item in arr]
y_arr= [item[1] for item in arr]
x_sorted_arr= [item[0] for item in sorted_arr]
y_sorted_arr= [item[1] for item in sorted_arr]

plt.plot(x_sorted_arr, y_sorted_arr, marker='o', linestyle='-', color='b', label='stair')
plt.scatter(x_arr, y_arr, marker='x', color='r', label='all points')

plt.xlabel('X')
plt.ylabel('Y')


plt.legend()

plt.grid(True)
plt.show()




