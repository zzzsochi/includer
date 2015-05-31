from types import ModuleType

from zope.dottedname.resolve import resolve


def resolve_str(name_or_func, module, default):
    """ Resolve and return object from dotted name
    """
    assert isinstance(name_or_func, str)
    resolved = resolve(name_or_func, module=module)

    if isinstance(resolved, ModuleType):
        if not hasattr(resolved, default):
            raise ImportError("{}.{}".format(resolved.__name__, default))

        resolved = getattr(resolved, default)

    if not callable(resolved):
        raise TypeError("{!r} is not callable"
                        "".format(resolved))

    return resolved


def include(_name_or_func, *args,
            _module=None, _default='includeme', **kwargs):
    """ Resolve and functions
    """
    if callable(_name_or_func):
        resolved = _name_or_func
    else:
        resolved = resolve_str(_name_or_func, _module, _default)

    resolved(*args, **kwargs)


class IncluderMixin:
    """ Mix to objects `include` method
    """
    _include_default = 'includeme'
    _include_module = None

    def include(self, _name_or_func, *args, **kwargs):
        if callable(_name_or_func):
            resolved = _name_or_func
        else:
            resolved = resolve_str(
                name_or_func=_name_or_func,
                module=self._include_module,
                default=self._include_default,
            )

        wrap = _IncluderWrapper(self, resolved.__module__)

        resolved(*((wrap,) + args), **kwargs)


class _IncluderWrapper(IncluderMixin):
    _include_object = None

    def __init__(self, obj, module):
        self._include_object = obj
        self._include_module = module

    def __getattr__(self, attr):
        return getattr(self._include_object, attr)

    def __setattr__(self, attr, value):
        if attr.startswith('_include_'):
            self.__dict__[attr] = value
        else:
            setattr(self._include_object, attr, value)
