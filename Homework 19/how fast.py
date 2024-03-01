import time


def benchmark_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.5f} seconds to complete.")
        return result

    return wrapper


@benchmark_time
def example_function():
    time.sleep(2)
    print("Function completed!")


@benchmark_time
def another_function():
    time.sleep(1)
    print("Function completed!")


example_function()
another_function()
