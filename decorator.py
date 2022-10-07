def author(name):

    def decorator(my_func):
    
        def create_new_func(*args, **kwargs):
    
            create_new_func._author = name
    
            return my_func(*args, **kwargs)

        return create_new_func

    return decorator

@author("Dany Longo")
def add2(num: int) -> int:
    return num  +   2

print(add2(0))
print(add2._author)