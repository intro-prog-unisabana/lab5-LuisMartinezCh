some_int = None
some_str = None

def set_globals(a,b):
    global some_str, some_int
    some_int = (a)
    some_str = (b)
def get_globals():
    return (some_int, some_str)

print(get_globals())
set_globals(10, "Hello")
print(get_globals())