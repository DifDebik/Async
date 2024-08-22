

def coroutine(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper


class BlaBlaException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('..........', message)

    return 'Returned from subgen()'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)
