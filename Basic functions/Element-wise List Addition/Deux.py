def add_two_lists(a, b):
    #return [sum(pair) for pair in zip(a, b)]
  return [x + y for x, y in zip(a, b)]
