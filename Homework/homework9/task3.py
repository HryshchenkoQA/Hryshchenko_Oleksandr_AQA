def print_function_name(func):
  def wrapper(*args, **kwargs):
    print(f"Calling function: {func.__name__}")
    return func(*args, **kwargs)
  return wrapper

@print_function_name
def add(a, b):
  return a + b

@print_function_name
def multiply(a, b):
  return a * b

print(add(1, 2))
print(multiply(3, 4))
