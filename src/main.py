import numpy as np

#  Creating array from list
arr_1d = np.array([1,2,3,4,5,6])
arr_2d = np.array([[1,2,3],[4,5,6]])

# List vs numpy array
py_list = [1,2,3]

def main():
    print("1D Array: ", arr_1d)
    print("2D Array: ", arr_2d)
    print("Python list multiplication: ", py_list*2)
    print("Python Array Multiplication: ", arr_1d*2)


if __name__ == "__main__":
    main()
