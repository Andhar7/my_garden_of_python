#import numpy as np

try:
    import numpy as np  # pyright: ignore[reportMissingImports]
except ImportError:
    numpy = None

# Challenge 1: Create arrays
print("====== Challenge 1: Create Arrays ======")

arr_1 = np.array([1, 2, 3, 4, 5])

arr_2 = np.array([10, 20, 30, 40, 50])

result_multiplay = arr_1 * arr_2

print(f"Here is result of multiplay: {result_multiplay}")

print(f"Array 1: {arr_1}")
print(f"Array 2: {arr_2}")

# Challenge 2: Vectorization (NO LOOPS!)
print("====== Challenge 2: Vectorization ======")

result_add = arr_1 + arr_2
print(f"Array_1 + Array_2 : {result_add}")

result_add = arr_1 * 2
print(f"Array_1 * 2 : {result_add}")

result_add = arr_1**2
print(f"Array_1 is squared : {result_add}")


# Challenge 3: Useful statistics
print("====== Challenge 3: Statistics ======")

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Data: {data}")

print(f"Sum: {np.sum(data)}")

print(f"Mean: {np.mean(data)}")
print(f"Std Dev: {np.std(data)}")

print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")


# Challenge 4: Matrix operations
print("====== Challenge 4: Matrix operations ======")

matrix = np.array(
    [[1, 2, 3, 5], 
     [4, 5, 6, 3], 
     [7, 8, 9, 3]]
    )
print(f"Matrix:\n{matrix}")

print(f"Shape: {matrix.shape}")

print(f"Sum of all: {np.sum(matrix)}")

print(f"Sum of each row: {np.sum(matrix, axis=1)}")
print(f"Sum of each column: {np.sum(matrix, axis=0)}")

# Challenge 5: Reshaping
print("====== Challenge 5: Reshaping ======")

flat = np.array([1,2,3,4,5,6])
reshaped = flat.reshape(2,3)

print(f"Original shape: {flat.shape}")
print(f"Reshaped (2,3) :\n {reshaped}") # Created two arrays [[1 2 3] [4 5 6]]

# Challenge 6: Dot product (matrix multiplication)
print("====== Challenge 6: Dot product ======")

a = np.array([1,2,3])
b = np.array([4,5,6])

dot_product = np.dot(a, b)

print(f"a = {a}")
print(f"b = {b}")
print(f"a · b = {dot_product}")
print(f"Calculation: 1*4 + 2*5 + 3*6 = {1*4 + 2*5 + 3*6}")


