################
from datetime import datetime
def decorator1(func):
    def wrapper():
        start = datetime.now()
        func()
        finish = datetime.now()
        print(finish-start)
    return wrapper

@decorator1
def func():
    for i in range(200):
        print(i)
#func()
###############
dictionary = {'func1':1,'func2':1,'func3':2,'func4':3}
@decorator1
def decorator2(func):
    def wrapper():
      if dictionary.has_key(func.__name__):
        print(dictionary.get(func.__name__))
      else:
        print(func())
    return wrapper

@decorator2
def func3():
    return 56

func3()