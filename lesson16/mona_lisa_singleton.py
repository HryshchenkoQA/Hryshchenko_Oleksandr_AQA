

def singleton(_class):
    def inner(*args):
        if not getattr(_class,'instance'):
    return inner