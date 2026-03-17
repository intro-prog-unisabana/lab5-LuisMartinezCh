some_int = None
some_str = None

def set_globals(a,b):
    global some_str, some_int
    some_int = int(a)
    some_str = str(b)
def get_globals():
    return (some_int, some_str)
