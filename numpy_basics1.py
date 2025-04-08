
import numpy as np 
# import random
# array1 = np.array([1,2,4,5,])
# array2 = np.array([2,4,6,8])

# array3 = array1 * array2 

# array4 = np.array([[1,2,3],[4,5,6]])



# a = np.array([[1,2,3,4,5,6,7,8],[2,3,4,5,2,6,7,9]])
# print(a)
# print(a[1,4])
# print(a[1, : ])
# x = np.zeros((2,2,2,2))

# x[:,0,1] = 9
# print(x)


# a = np.array([
#    [ [1,3,4],[2,3,4],[4,5,6]],
#    [[2,4,6],[6,4,2],[11,14,17]],
#    [[13,19,10],[20,30,49],[12,67,45]]
# ])
# print(a.ndim)
# print("---------------------------")
# print(a)
# print("---------------------------")
# print(a[2,2,0])
# print(a[: : 2])



# b = np.zeros((2,2,3,2), dtype="float32")
# print(b)


# t = np.full_like(a, 6)
# print(t)


# r = np.random.rand(2,3)
# print(r)



# ran= np.random.randint(-10,20, a.shape)
# print(ran)



# new = np.identity(5)
# print(new)



# class nums: 
#     def display(self):
#         print("This is initiated")

      
# class integers(nums):
#     def prints(self):
#         print("This is also a number but only non decimals or non fractions")





# num1 = nums()
# int1 = integers()

# # int1.display()




# a = [1,5,6,3,6,8,3,2]
# b = filter(lambda x : x%2 == 0)




# output = np.ones((5,5), dtype = 'int32')

# z = np.zeros((3,3))
# z[1,1] = 9
# output[1:-1, 1:-1] = z 
# print(z)
# print(output)




# a = np.ones((3,2))
# b = np.full((2,3), 2)
# print(np.matmul(a,b))
# d = np.matmul(a,b)
# print(np.linalg.det(d))


# c = np.identity(3)
# print(c)
# print(np.linalg.det(c))



# arrnew = np.array([
#        [ [1,3,4],[2,3,4],[4,5,6]],
#    [[2,4,6],[6,4,2],[11,14,17]],
#    [[13,19,10],[20,30,49],[12,67,45]]
# ])

# for i in arrnew :
#     for x in i :
#         for z in x :
#             print(z+5)


import numpy as np

# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

# print(x)



# listnum = [1,2,3,4,5,5]

# x = list(filter(lambda x: x%2==0, listnum))
# z = np.array(x)
# print(type(z))
# print(z.shape)

arr = [1,4,5,6,23,3,21,45]

print("Define the count of the number : ")

numbers = list(map(lambda x : x +2  , arr ))
print(numbers)

even_number = list(filter(lambda x: x % 2 == 0 , numbers))
print(even_number)




even = list(map(int, input("numbers: ").split()))
print(even)

