import time
def time_delay(function):
    def wrapper_function():
        time.sleep(3)
        function()
        function()
    return wrapper_function

@time_delay
def say_hi():
    print('Hi')

@time_delay
def say_hello():
    print('hello')

def say_bye():
    print('bye')

output=time_delay(say_bye)
output()