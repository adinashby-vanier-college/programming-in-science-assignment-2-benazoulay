# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    max_val = second_max = None

    for num in numbers:
        if max_val is None or num > max_val:
            second_max = max_val
            max_val = num  
        elif num != max_val and (second_max is None or num > second_max):
            second_max = num  
    
    return (max_val, second_max)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_list = list(set(numbers))
    unique_list.sort()
    return unique_list
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    cumulative = []
    current_sum = 0
    for num in arr:
        current_sum += num
        cumulative.append(current_sum)
    return cumulative

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    result = []
    for i in range(0, len(lst), step):
        result.append(lst[i])
    return result

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    result = 0
    for x, y in zip(list1, list2):
        result += x * y
    return result

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows_A = len(matrix1)
    cols_A = len(matrix1[0])
    rows_B = len(matrix2)
    cols_B = len(matrix2[0])

    if cols_A != rows_B:
        return None

    result = [[0, 0], [0, 0]]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
   