import time
# print(current_time)  # seconds since Jan 1st, 1970

current_time = time.time()
print(current_time)
# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        print(f"{function.__name__} run speed {time.time()-current_time}s")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        numbers = i * i
        # print(i * i)


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        numbers = i + i
        # print(i * i)

fast_function()
slow_function()