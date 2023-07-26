#!/usr/bin/env python3

def generate_list(n):
  """Generates a list of integers from 1 to n, inclusive."""
  result_list = []
  for i in range(1, n + 1):
    result_list.append(i)
  return result_list


if __name__ == "__main__":
  n = 10
  print(generate_list(n))
