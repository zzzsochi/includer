def includeme(obj):
    obj.append(('init_includeme', obj))
    return obj


def func(obj):
    obj.append(('init_func', obj))
    obj.include('.for_include.func_func')
    return obj
