import names
from task2 import benchmark

@benchmark
def list_of_names(n: int) -> list:
    ''' 
    This function is creating a LIST OF REAL FULL NAMES. 
    Please enter a number of names as argument.
    '''
    listt = []
    for i in range(n):
        name = names.get_full_name()
        listt.append(name)
    return listt

# classmates = list_of_names(10)
# print(classmates)
list_of_names(10)