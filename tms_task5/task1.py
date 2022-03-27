import names
from task2 import benchmark

@benchmark
def list_of_names(n: int) -> list:
    ''' 
    This function is creating a LIST OF REAL FULL NAMES. 
    Please enter a number of names as argument.
    '''
    return [names.get_full_name() for i in range(n)]

classmates = list_of_names(1)
print(classmates)