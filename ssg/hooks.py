_callbacks = dict()


def register(hook, order=0):
    def register_callback(func):
        _callbacks.setdefault(hook, {}).setdefault(order, []).append(func)
        return func
    return register_callback


def event(hook, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[order]:
            func(*args)


def filter(hook, value, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[order]:
            value = func(value, *args)
    return value
