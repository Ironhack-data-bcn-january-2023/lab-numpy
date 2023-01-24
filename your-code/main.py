#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(0,10,size = (2,3,5))
a = np.random.random((2,3,5))


#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))


#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

a.size == b.size



#8. Are you able to add a and b? Why or why not?

# a and b have different shapes, they cant be added.


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a+c

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a,d)

#d == a+b.transposed , consering b is a numpy array with 1's as values


#12. Multiply a and c. Assign the result to e.

e = a*c


#13. Does e equal to a? Why or why not?

False in (a == e)

# a == e is a numpy array. given that e = a * (matrix of the same shape, with 1 as all values), its logical that the output of the multiplication is the same


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f =  np.zeros(shape=(2,3,5))


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for ind1, dimension in enumerate(d):
    for ind2, row in enumerate(dimension):
        for ind3, i in enumerate(row):
            if i > d_min and i < d_mean:
                f[ind1][ind2][ind3] = 25
            elif i > d_mean and i < d_max:
                f[ind1][ind2][ind3] = 75
            elif i == d_mean:
                f[ind1][ind2][ind3] = 50
            elif i == d_min:
                f[ind1][ind2][ind3] = 0
            elif i == d_max:
                f[ind1][ind2][ind3] = 100


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
f =  np.zeros(shape=(2,3,5))
f = f.tolist()

for ind1, dimension in enumerate(d):
    for ind2, row in enumerate(dimension):
        for ind3, i in enumerate(row):
            if i > d_min and i < d_mean:
                f[ind1][ind2][ind3] = "B"
            elif i > d_mean and i < d_max:
                f[ind1][ind2][ind3] = "D"
            elif i == d_mean:
                f[ind1][ind2][ind3] = "C"
            elif i == d_min:
                f[ind1][ind2][ind3] = "A"
            elif i == d_max:
                f[ind1][ind2][ind3] = "E"