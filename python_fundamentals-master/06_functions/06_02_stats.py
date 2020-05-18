'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''
import math
example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  # define the function here
  print('\nFor example list the values are:\n')
  print(f'\tMax: {max(example_list)}')
  print(f'\tMin: {min(example_list)}')
  print(f'\tSum: {sum(example_list)}')
  print(f'\tAverage: {(sum(example_list)/len(example_list))}\n')
  

# call the function below here
stats()