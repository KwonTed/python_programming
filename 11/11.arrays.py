import numpy as np

print(np.__version__)

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.shape)

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a[0])

a[0] = 10
print(a)

print(a[:3])

b = a[3:]
print(b)
b[0] = 40
print(a)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

print(a[1, 3])

print(a.ndim)

print(a.shape)
print(len(a.shape) == a.ndim)

print(a.size)
import math
print(a.size == math.prod(a.shape))

print(a.dtype)

print(np.zeros(2))
print(np.ones(2))
print(np.empty(2))
print(np.arange(4))
print(np.arange(2, 9, 2))
print(np.linspace(0, 10, num=5))
x = np.ones(2, dtype=np.int64)
print(x)


arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))
a = np.array([1, 2, 3, 4])
print(a)
b = np.array([5, 6, 7, 8])
print(b)
print(np.concatenate((a, b)))
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))


array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print(array_example.ndim)
print(array_example.size)
print(array_example.shape)

a = np.arange(6)
print(a)
b = a.reshape(3, 2)
print(b)
print(np.reshape(a, shape=(1, 6), order='C'))

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
a2 = a[np.newaxis, :]
print(a2.shape)
row_vector = a[np.newaxis, :]
print(row_vector.shape)
col_vector = a[:, np.newaxis]
print(col_vector.shape)
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
b = np.expand_dims(a, axis=1)
print(b.shape)
c = np.expand_dims(a, axis=0)
print(c.shape)

data = np.array([1, 2, 3])
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
five_up = (a >= 5)
print(a[five_up])
divisible_by_2 = a[a%2==0]
print(divisible_by_2)
c = a[(a > 2) & (a < 11)]
print(c)
five_up = (a > 5) | (a == 5)
print(five_up)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b)
list_of_coordinates= list(zip(b[0], b[1]))
for coord in list_of_coordinates:
    print(coord)
print(a[b])
not_there = np.nonzero(a == 42)
print(not_there)


a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = a[3:8]
print(arr1)
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])
print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))
x = np.arange(1, 25).reshape(2, 12)
print(x)
print(np.hsplit(x, 3))
print(np.hsplit(x, (3, 4)))
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :]
print(b1)
b1[0] = 99
print(b1)
print(a)
b2 = a.copy()
print(b2)

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)
print(data - ones)
print(data * ones)
print(data / ones)

a = np.array([1, 2, 3, 4])
print(a.sum())

b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))
print(b.sum(axis=1))

data = np.array([1.0, 2.0])
print(data * 1.6)
print(data.max())
print(data.min())
print(data.sum())

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
print(a.sum())
print(a.max())
print(a.min())
print(a.min(axis=0))

data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)
print(data[0, 1])
print(data[1:3])
print(data[0:2, 0])
print(data.max())
print(data.min())
print(data.sum())

data = np.array([[1, 2], [5, 3], [4, 6]])
print(data)
print(data.max(axis=0))
print(data.max(axis=1))

data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
print(data + ones)

data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data + ones_row)

print(np.ones((4, 3, 2)))

print(np.ones(3))
print(np.zeros(3))
rng = np.random.default_rng()
print(rng.random(3))
print(np.ones((3, 2)))
print(np.zeros((3, 2)))
print(rng.random((3, 2)))

print(rng.integers(5, size=(2, 4)))
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
print(unique_values)
unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list)
unique_values, occurrence_count = np.unique(a, return_counts=True)
print(occurrence_count)
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
unique_values = np.unique(a_2d)
print(unique_values)
unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)
unique_rows, indices, occurrence_count = np.unique(
     a_2d, axis=0, return_counts=True, return_index=True)
print(unique_rows)
print(indices)
print(occurrence_count)

data.reshape(2, 3)
data.reshape(3, 2)
arr = np.arange(6).reshape((2, 3))
print(arr)
print(arr.transpose())
print(arr.T)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = np.flip(arr)
print('Reversed Array: ', reversed_arr)
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr = np.flip(arr_2d)
print(reversed_arr)
reversed_arr_rows = np.flip(arr_2d, axis=0)
print(reversed_arr_rows)
reversed_arr_columns = np.flip(arr_2d, axis=1)
print(reversed_arr_columns)
arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)
arr_2d[:,1] = np.flip(arr_2d[:,1])
print(arr_2d)

x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x.flatten())
a1 = x.flatten()
a1[0] = 99
print(x)
print(a1)
a1 = x.flatten()
a2 = x.ravel()
a2[0] = 98
print(x)
print(a2)