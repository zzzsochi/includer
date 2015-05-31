def includeme(obj=None):
    if obj is not None:
        obj.append(('includeme', obj))

    return obj


def func(obj=None):
    if obj is not None:
        obj.append(('func', obj))

    return obj


def func_func(obj):
    obj.append(('func_func', obj))
    obj.include('.func')


not_callable = 'not callable data'
