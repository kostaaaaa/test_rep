def benchmark(func):
    '''
    This decorator shows how long the function (with 1 argument) takes to complete.
    '''
    import time
    def wrapper(arg):
        start_time = time.time()
        return_value = func(arg)
        finish_time = time.time()
        ex_time = finish_time - start_time
        print(f'This function was executed in {ex_time}.')
        return return_value
    return wrapper