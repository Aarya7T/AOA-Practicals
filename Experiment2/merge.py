import os
import random
import time

def generate_and_store_numbers():
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))
    
    num_numbers = int(input("Enter the number of random numbers to generate: "))
    file_name = input("Enter the name of the file to save the numbers: ")
    path = input("Enter the path where the file should be saved:")

    random_numbers = [random.randint(lower_limit, upper_limit) for _ in range(num_numbers)]
    random_file_path = os.path.join(path, file_name.replace('.txt', '_random.txt'))

    with open(random_file_path, 'w') as file:
        for number in random_numbers:
            file.write(str(number) + '\n')

    print(f"{num_numbers} random numbers generated and stored in {random_file_path}.")

    sort_and_store_numbers(random_file_path)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def sort_and_store_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    if len(numbers) < 30:
        start_time = time.time()
        insertion_sort(numbers)
        time_taken = time.time() - start_time
        print(f"Insertion Sort took {time_taken:.5f} seconds")
    else:
        start_time = time.time()
        merge_sort(numbers)
        time_taken = time.time() - start_time
        print(f"Merge Sort took {time_taken:.5f} seconds")

    sorted_file_path = file_path.replace('_random.txt', '_sorted.txt')
    with open(sorted_file_path, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

    print(f"Sorted numbers are stored in {sorted_file_path}")

generate_and_store_numbers()

