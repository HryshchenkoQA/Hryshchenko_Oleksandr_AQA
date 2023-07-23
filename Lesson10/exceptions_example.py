#int('text')
#raise Exception('q')
#raise Exception('Not supported opperation')

def sum(a,b):
    try:
        assert a != b
        return a+b
    except AssertionError as e:
        print('we are i assertion error')
    except TypeError as e:
        print('we are in Type error')
    else:
        print('we are in the else situation')
    finally:
        print('final block of code')
    print('this is code after finally')
        #pass
        #print('Not supported type')

    #return a+b

#sum(1,'text')
#sum('text',1)
sum('1',1)
sum(1,2)