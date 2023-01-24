#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a=np.random.random((2,3,5))


#4. Print a.

print('This is the array A' , a)
print('and its shape', np.shape(a))


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.ones((5,2,3))


#6. Print b.

print(f'This is the array B', b)
print('and its shape', np.shape(b))


#7. Do a and b have the same size? How do you prove that in Python code?

print('Do they have the same size?' ,a.size==b.size)



#8. Are you able to add a and b? Why or why not?
try:
        c = np.add(a,b)
        print (f'The summ is : {c}')
except ValueError:
        print ('You cannot add different shape arrays')



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
# shape of a = (2,3,5)
# shape of b = (5,2,3)
#print (b)
c = b.transpose(1,2,0)
#print (c) 

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?


print ('shape of a', a.shape)
print ('shape of b', b.shape)
print('Are they the same shape?', a.shape==b.shape)

d = a+c
print ('the summ of a + c is', d)



#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print ( 'array a :', a)
print ( 'array d :', d)



#12. Multiply a and c. Assign the result to e.
e = a*c
print ( 'Multiply a and c = e ' , e) 

#13. Does e equal to a? Why or why not?

print('Does e equal to a?', a == e)
print('Are all the values equal?', not(False in a == e))


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max= d.max()
d_min= d.min()
d_mean= d.mean()
print('The maximum value in the array d is: ',d_max)
print('The minimum value in the array d is: ',d_min)
print('The mean of the values in the array d is: ', round(d_mean))


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f= np.empty((2,3,5))
print ( 'This is an empty arrar f: ', f)
print ('shape of f', f.shape)

print (f[0][0][0])

'''
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
'''
print(d[0,0,0])
d.astype(int)
f.astype(int)

        
        

for i in range(0,d.shape[0]):
        for x in range(0,d.shape[1]):
                for y in range(0,d.shape[2]):

                        if d[i,x,y] > d_min and d[i,x,y] < d_mean:
                                f[i,x,y] = 25
                        elif d[i,x,y] < d_max and d[i,x,y] > d_mean:
                                f[i,x,y] = 75
                        elif d[i,x,y] == d_mean:
                                f[i,x,y] = 50
                        elif d[i,x,y] == d_max:
                                f[i,x,y] = 100
                        elif d[i,x,y] == d_min:
                                f[i,x,y] = 0
print ('The f array is: ', f)




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

d_comprovation= np.array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
f_comprovation= np.empty((2,3,5))
d_max= d_comprovation.max()
d_min= d_comprovation.min()
d_mean= d_comprovation.mean()
for i in range(0,d_comprovation.shape[0]):
        for x in range(0,d_comprovation.shape[1]):
                for y in range(0,d_comprovation.shape[2]):

                        if d_comprovation[i,x,y] > d_min and d_comprovation[i,x,y] < d_mean:
                                f_comprovation[i,x,y] = 25
                        elif d_comprovation[i,x,y] < d_max and d_comprovation[i,x,y] > d_mean:
                                f_comprovation[i,x,y] = 75
                        elif d_comprovation[i,x,y] == d_mean:
                                f_comprovation[i,x,y] = 50
                        elif d_comprovation[i,x,y] == d_max:
                                f_comprovation[i,x,y] = 100
                        elif d_comprovation[i,x,y] == d_min:
                                f_comprovation[i,x,y] = 0
print ('The comprovation array f array is: ', f_comprovation)

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
g = np.empty((2,3,5,),dtype=str)
print ( 'my d array is: ', d)
print ('my empty string array : ', g)
d_max= d.max()
d_min= d.min()
d_mean= d.mean()
print('The maximum value in the array d is: ',d_max)
print('The minimum value in the array d is: ',d_min)
print('The mean of the values in the array d is: ', round(d_mean))
for i in range(0,d.shape[0]):
        for x in range(0,d.shape[1]):
                for y in range(0,d.shape[2]):

                        if d[i,x,y] > d_min and d[i,x,y] < d_mean:
                                g[i,x,y] = 'A'
                        elif d[i,x,y] < d_max and d[i,x,y] > d_mean:
                                g[i,x,y] = 'B'
                        elif d[i,x,y] == d_mean:
                                g[i,x,y] = 'C'
                        elif d[i,x,y] == d_max:
                                g[i,x,y] = 'D'
                        elif d[i,x,y] == d_min:
                                g[i,x,y] = 'E'
print ( 'My string array is : ', g)