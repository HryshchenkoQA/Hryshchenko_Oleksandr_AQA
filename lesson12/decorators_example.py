def percent(func):
    def inner(*args, **kwargs):
        header, footer = "%" * 20, "%" * 20
        return f"{header}\n{func(*args, **kwargs)}\n{footer}"
    return inner

def and_symbol(func):
    def inner(*args, **kwargs):
        header, footer = "&" * 20, "&" * 20
        return f"{header}\n{func(*args, **kwargs)}\n{footer}"
    return inner

def add_footer_header(sign, quantity):
    def middle_level(func):
        def inner(some_msg):
            footer = sign * quantity
            header = sign * quantity
            return f"{header}\n{some_msg}\n{footer}"
        return inner
    return middle_level

# @and_symbol
# @percent
@add_footer_header("#", 10)
#декораторы используются сверху вниз
def hi(msg):
    return "***\n" + msg + "\n***"
print(hi("Hello my fellow friends")) 
