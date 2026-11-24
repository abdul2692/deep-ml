def min_max(x: list[float]) -> list[float]:
  """Perform Min-Max normalization to scale values to [0, 1].

  Args:
      x: A list of numerical values.

  Returns:
      A new list of floats with values normalized to [0, 1].
  """
  if not x:
    return []

  min_val = min(x)
  max_val = max(x)
  value_range = max_val - min_val

  if value_range == 0:
    return [0.0] * len(x)

  return [(float(val) - min_val) / value_range for val in x]