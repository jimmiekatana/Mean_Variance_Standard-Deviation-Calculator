

import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    result = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }

    return result
  input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

  result = calculate(input_list)

  for key, value in result.items():
      print(key)
      if key != 'sum':
          for axis, val in zip(['axis1', 'axis2', 'flattened'], value):
              print(f"{axis}: {val}")
      else:
          print(f"{key}: {value}")