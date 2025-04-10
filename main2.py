import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))

b = np.array([[1, 2], [3, 4]])
print(b)
print(type(b))

zeros = np.zeros((2, 3))
print(zeros)
print(type(zeros))

# ones = np.ones((2 ,3))
# print(ones)
# print(type(ones))
#
# arrange = np.arange(0, 10, 2)
# print(arrange)
# print(type(arrange))
#
# linspace = np.linspace(0, 1, 5)
# print(linspace)
# print(type(linspace))
#
# _random = np.random.rand(2, 3)
# print(_random)
#
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a)
# print(a.shape)
#
# print(a.reshape(2, 3))
#
# a = np.array([1, 2, 3, 4 ,5])
# print(a[0])
# print(a[1:3])
#
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
# print(b[0, 1])
#
# print(b[:, 1])
#
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a+b)
# print(a * 2)
# print(np.sin(a))
#
# a = np.array([[1, 2], [3, 4]])
# print(a)
# b = np.array([[5, 6], [7, 8]])
# print(b)
# print(np.dot(a, b))
# print(a@b)
#
#
# a = np.array([[1, 2], [3, 4]])
# print(a)
# b = np.array([10, 20])
# print(b)
# print(a+b)
# print()
# print(a@b)
#
# print("-")
# a = np.array([1, 2, 3, 4])
# print(a)
# print(np.sum(a))
# print(np.mean(a))
# print(a.mean())
# print(np.max(a))
# print(a.max())
# print(np.min(a))
# print(a.min())
#
# np.save("array.npy", a)
# load_array = np.load("array.npy")
# print(load_array)
#
# print("---------")
# np.savetxt("data.txt", a)
# data = np.loadtxt("data.txt")
# print(type(data))
#
# print(np.sum(a, axis=0))
