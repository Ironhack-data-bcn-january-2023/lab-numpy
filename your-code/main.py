#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a1 = np.random.randint(100, size = (2, 3, 5))
a2 = np.random.randint(25, 45, size = (2, 3, 5))
a3 = np.random.rand(2, 3, 5)

#here, the .astype(np.float32) is used to cast or change the datatype of the array elements from default float64 to float32. It's an optional step, depending on the use case and the datatype requirement of the array.    
a4 = np.random.rand(3, 2, 5).astype(np.float32)


# this creates a Numpy array that's filled with numeric values. Those numeric values are drawn from within the specified range, specified by low to high . The function will randomly select N values from that range, where N is given by the size parameter. Multiplying by 10, scales the values up.

a5 = np.random.random_sample((3, 2, 5))*10




#The low parameter specifies the lower boundary of the interval of random numbers to generate. The high parameter specifies the upper boundary of the interval of random numbers to generate. And the size parameter specifies the shape of the output array, which is a 3D array with shape (3, 2, 5) in this case.

a6= np.random.uniform(low=0, high=2, size=(3, 2, 5))

#4. Print a.

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size == b.size)


#8. Are you able to add a and b? Why or why not?


print(f"It's not possible to add a1 and b, because they have different shape. This opperation will return the following error: 'ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3)'")


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1, 2, 0)

#this method of transposing works beacause it takes the index positions in the tuple that defines the shape of the array, and then it reassigns the original shape values for array b, and modifies it to fit the new positions.


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = c + a1

#Now it worked, because both arrays have the exact same shape.

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(d)
print(a1)

#Adding and array of ones to another array of the same shape, is like doing a +=1 increment for a regular numeric variable

#12. Multiply a and c. Assign the result to e.

e = a1 * c

#13. Does e equal to a? Why or why not?

print(e == a1)
np.array_equal(a1, e)

#this returns an array of True values, because multiplying the values of a1 (random values) by the values of c (all ones), will result in a new array with values matching those in arra a1


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
print(d_max)

d_min = d.min()
print(d_min)

d_mean = d.mean()
print(d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2, 3, 5), like=d)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        for k in range(f.shape[2]):
            if d[i, j, k] == d_min:
                f[i, j, k] = 0
            elif d[i, j, k] > d_min and d[i, j, k] < d_mean:
                f[i, j, k] = 25
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 50
            elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                f[i, j, k] = 75
            elif d[i, j, k] == d_max:
                f[i, j, k] = 100



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

g = np.empty((2, 3, 5), dtype=str)

for i in range(g.shape[0]):
    for j in range(g.shape[1]):
        for k in range(g.shape[2]):
            if d[i, j, k] == d_min:
                g[i, j, k] = "A"
            elif d[i, j, k] > d_min and d[i, j, k] < d_mean:
                g[i, j, k] = "B"
            elif d[i, j, k] == d_mean:
                g[i, j, k] = "C"
            elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                g[i, j, k] = "D"
            elif d[i, j, k] == d_max:
                g[i, j, k] = "E"
                
print(g)



