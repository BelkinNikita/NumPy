import numpy as np
# using of Numpy as np is a recommended convention 



# arternative to the array.array. numpy.array gives an optimized solution for large-scaled mathematical computations
arr = np.array([[1,2,3],
                [4,5,6], 
                [4,5,7], 
                [8,9,10]])
raa = np.array([[10,9,8],
                [7,6,5], 
                [7,6,5], 
                [4,3,2]])

#Generate arrays
print("Zeros: "             + str( np.zeros((2,5))                             )            ) # ... (col, rows) of zeros
print("Ones: "              + str( np.ones((2,5))                              )            ) # ... (col, rows) of ones
print("Empty: "             + str( np.empty((2,5))                             )            ) # ... (col, rows) of random values
print("Arange: "            + str( np.arange(0,10)                             )            ) # ... in range from X to Y
print("Linspace: "          + str( np.linspace(0,10,5, False, True)            )            ) # ... in range from X to Y with the Z num of values
print("Full: "              + str( np.full((2,3),7)                            )            ) # ... filled by Z
print("logspace: "          + str( np.logspace(1,3,5)                          )            ) # ... from log10^X to log10^Y in range(Z)
print("Diagonal Matrix: "   + str( np.diag([2,4,7,9,11])                       )            ) # ... of the diagonal matrix (args as diagonal numbers)
print("Identity: "          + str( np.identity(8)                              )            ) # works as ⬆np.diag⬆, but all numbers are identical
print("Eye: "               + str( np.eye(8, 7, k=1)                           )            ) # works as ⬆np.identity⬆, bit has additional args
print("From function: "     + str( np.fromfunction(lambda i,j:i+j,(3,3))       )            ) # returns a new array

# Array Manipulation
print("Ravel  : "           + str( np.ravel(arr)                               )            ) # returns the array as a one-dimensional one 
print("Transpose  : "       + str( np.transpose(arr)                           )            ) # returns the array with reversed axes
print("Swapaxes  : "        + str( np.swapaxes(arr,0,1)                        )            ) # works as ⬆np.transpos⬆, but works only for two axes
print("Concatenate  : "     + str( np.concatenate([arr,raa])                   )            ) # adds the second array as additional columns 
print("Vstack  : "          + str( np.vstack([arr,raa])                        )            ) # works as ⬆np.concatenate⬆, NEED MORE INFORMATION
print("Stack  : "           + str( np.stack([arr,raa])                         )            ) # combines the second array through an empty line
print("Hstack : "           + str( np.hstack([arr,raa])                        )            ) # adds the second array as additional rows
print("Split  : "           + str( np.split(arr,2)                             )            ) # splits the array on parts
print("Tile  : "            + str( np.tile(arr,(2,3))                          )            ) # repeats X-times vertically and Y-times horizontally 
print("Repeat  : "          + str( np.repeat(arr,3)                            )            ) # returns a one-dimensional array with repeated values xxyyzz

# Array Propeties
print("np.array: \n"        + str( arr                                         )            ) # np.array
print("Dimensions: "        + str( arr.ndim                                    )            ) # num of dimensions
print("Rows and columns: "  + str( arr.shape                                   )            ) # num of columns and rows
print("Elements: "          + str( arr.size                                    )            ) # num of elements      
print("Type: "              + str( arr.dtype                                   )            ) # data-type
print("Itemsize  : "        + str( arr.itemsize                                )            ) # memory consumptiom

# Trigonometry
print("sin  : "             + str( np.sin(180)                                 )            ) # sine
print("cos  : "             + str( np.cos(180)                                 )            ) # cosine 
print("tan  : "             + str( np.tan(180)                                 )            ) # tangent 
print("arcsin  : "          + str( np.arcsin(180)                              )            ) # arcsine
print("arccos  : "          + str( np.arccos(180)                              )            ) # arccosine
print("arctan  : "          + str( np.arctan(180)                              )            ) # arctangent
print("deg2rad  : "         + str( np.deg2rad(180)                             )            ) # from degrees to radians
print("rad2deg  : "         + str( np.rad2deg(180)                             )            ) # from radians to degrees

# Math
print("Add  : "             + str( np.add(arr,raa)                             )            ) # combines values, in ARRAYS combines indexes
print("Subtract  : "        + str( np.subtract(arr,raa)                        )            ) # substracts values, in ARRAYS substracts indexes
print("Multiply  : "        + str( np.multiply(arr,raa)                        )            ) # multiplies values, in ARRAYS multiplies indexes
print("Divide  : "          + str( np.divide(arr,raa)                          )            ) # divides values, in ARRAYS divides indexes
print("power  : "           + str( np.power(arr,2)                             )            ) # raises to the power of X
print("sqrt  : "            + str( np.sqrt(arr)                                )            ) # square root
print("abs  : "             + str( np.abs(arr)                                 )            ) # absolute value
print("sign  : "            + str( np.sign(arr)                                )            ) # returns 1 for positive values and vice versa
print("exp  : "             + str( np.exp(arr)                                 )            ) # exponential
print("log  : "             + str( np.log(arr)                                 )            ) # natural logarithm
print("log10  : "           + str( np.log10(arr)                               )            ) # base-10 logarithm
print("mod  : "             + str( np.mod(arr,3)                               )            ) # a remainder of division

# Statistics
print("mean  : "            + str( np.mean(arr)                                )            ) # calculates an arithmetic mean 
print("median  : "          + str( np.median(arr)                              )            ) # calculates a weighted average 
print("std  : "             + str( np.std(arr)                                 )            ) # calculates the deviation between numbers
print("var  : "             + str( np.var(arr)                                 )            ) # calculates a variance that how far are numbers from average value
print("min  : "             + str( np.min(arr)                                 )            ) # returs the min
print("max  : "             + str( np.max(arr)                                 )            ) # returns the max
print("sum  : "             + str( np.sum(arr)                                 )            ) # returns the sum
print("prod  : "            + str( np.prod(arr)                                )            ) # multiplies all values with each other
print("percentile  : "      + str( np.percentile(arr,90)                       )            ) # returns the mean of the most high values     

# Random
sh = np.random.shuffle([1,2,3,4,5,6])
print("rand  : "            + str( np.random.rand(1,5)                         )            ) # absolute random
print("randn  : "           + str( np.random.randn(1,5)                        )            ) # Gaussian random
print("randint  : "         + str( np.random.randint(0,10,(3,3))               )            ) # random integers from X to Y (columns, rows)
print("choice  : "          + str( np.random.choice([1,2,3,4])                 )            ) # random choice
print("shuffle  : "         + str( sh                                          )            ) # mixs up the array
print("seed  : "            + str( np.random.seed(0)                           )            ) # random number

# Sort
print("sort  : "            + str( np.sort([10,5,3,6,8,3], kind='quicksort')   )            ) # sorts by: 'quicksort', 'mergesort', 'heapsort', or 'stable'
print("argsort  : "         + str( np.argsort([4,5,3,6,8,3], kind='quicksort') )            ) # sorts, but instead values - indexes
#print("partition  : "       + str( np.partition(raa, -2)     )            ) # NEED INFO

# Logic
print("logical_and  : "     + str( np.logical_and(3>1,4<5)                     )            ) # if all are True
print("logical_or  : "      + str( np.logical_or(2>1,8<5)                      )            ) # if any is True
print("logical_not  : "     + str( np.logical_not(3<1)                         )            ) # if not True 
print("all  : "             + str( np.all([1,2,3,4,5])                         )            ) # checks for > 0
print("any  : "             + str( np.any([True,False,True,False])             )            ) # tests for True        
