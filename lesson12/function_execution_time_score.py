import datetime
def time_function(func):
    def timer(*args, **kwargs):
        start = datetime.datetime.now()
        result_function = func(*args, **kwargs)
        end = datetime.datetime.now() -start
        print(end - start)
        return result_function
    return timer

@time_function
def mega_math(first_value, second_value):
    return first_value*second_value
print(mega_math(5,10))

