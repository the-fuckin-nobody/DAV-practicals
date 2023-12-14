'''
Do the following uding pandas series:
1. Create a series with 5 elements. Display the series sorted on index and values separately.
2. Create a series with N elements with some duplicate values. Find the minimum and maximum ranks assigned to the valuesusing 'first' and 'max' methods.
3. Display the index value of the minimum anf the maximum elements of a series
'''

import pandas as pd
 
# Create a series with 5 elements
data = [1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)
 
# Display the series sorted on index
print("Series sorted by index:")
print(s.sort_index())
 
# Display the series sorted on values
print("Series sorted by values:")
print(s.sort_values())
 
# Create a series with N elements with some duplicate values
data = [1, 1, 2, 3, 3, 5]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)
 
# Find the minimum and maximum ranks assigned to the values using 'first' and 'max' methods
min_rank = s.rank(method='first')
max_rank = s.rank(method='max')
 
# Display the minimum and maximum ranks
print("Minimum rank:")
print(min_rank)
 
print("Maximum rank:")
print(max_rank)
 
# Display the index value of the minimum and maximum element of a Series
min_index = s.idxmin()
max_index = s.idxmax()
 
print("Index of minimum value:")
print(min_index)
 
print("Index of maximum value:")
print(max_index)
 
