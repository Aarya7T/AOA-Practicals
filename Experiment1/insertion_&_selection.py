import os
import time
import random

start = time.time()

def generate_and_store_numbers():
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))
    num_numbers = int(input("Enter the number of random numbers to generate: "))
    file_name = input("Enter the name of the file to save the numbers: ")
    path = input("Enter the path where the file should be saved: ")

    random_numbers = [random.randint(lower_limit, upper_limit) for _ in range(num_numbers)]
    
    full_path = os.path.join(path, file_name)

    with open(full_path, 'w') as file:
        for number in random_numbers:
            file.write(str(number) + '\n')
    
    sort_and_store_numbers(full_path)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def sort_and_store_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    sort_method = input("Choose a sorting method (insertion/selection): ").lower()
    start_sort = time.time()
    if sort_method == 'insertion':
        insertion_sort(numbers)
    elif sort_method == 'selection':
        selection_sort(numbers)
    else:
        print("Invalid sorting method selected. Using insertion sort by default.")
        insertion_sort(numbers)

    sorted_file_path = file_path.replace(".txt", f"_{sort_method}_sorted.txt")
    with open(sorted_file_path, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

    end_sort = time.time()
    print(f"Time taken to sort and store numbers using {sort_method} sort: {end_sort - start_sort} seconds")
    print(f"Sorted numbers are stored in {sorted_file_path}.")

generate_and_store_numbers()

end = time.time()


