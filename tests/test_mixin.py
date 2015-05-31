import pytest

from includer import IncluderMixin, _IncluderWrapper


@pytest.fixture(scope='function')
def obj():
    class Obj(IncluderMixin, list):
        pass

    return Obj()


def test__includeme(obj):
    obj.include('tests.for_include')
    assert len(obj) == 1
    assert obj[0][0] == 'includeme'
    assert isinstance(obj[0][1], _IncluderWrapper)
    assert obj[0][1]._include_object is obj
    assert obj[0][1]._include_module == 'tests.for_include'


def test__func(obj):
    obj.include('tests.for_include.func')
    assert len(obj) == 1
    assert obj[0][0] == 'func'
    assert isinstance(obj[0][1], _IncluderWrapper)
    assert obj[0][1]._include_module == 'tests.for_include'


def test___real_func(obj):
    from .for_include import func
    obj.include(func)
    assert len(obj) == 1
    assert obj[0][0] == 'func'
    assert isinstance(obj[0][1], _IncluderWrapper)
    assert obj[0][1]._include_module == 'tests.for_include'


def test__pkg_includeme(obj):
    obj.include('tests')
    assert len(obj) == 1
    assert obj[0][0] == 'init_includeme'
    assert isinstance(obj[0][1], _IncluderWrapper)
    assert obj[0][1]._include_module == 'tests'


def test__pkg_func(obj):
    obj.include('tests.func')
    assert len(obj) == 3
    assert obj[0][0] == 'init_func'
    assert isinstance(obj[0][1], _IncluderWrapper)
    assert obj[0][1]._include_module == 'tests'


def test_deeper(obj):
    obj.include('tests.for_include.func_func')
    assert len(obj) == 2

    assert obj[0][0] == 'func_func'
    assert isinstance(obj[0][1], _IncluderWrapper)
    assert obj[0][1]._include_module == 'tests.for_include'

    assert obj[1][0] == 'func'
    assert isinstance(obj[1][1], _IncluderWrapper)
    assert obj[1][1]._include_module == 'tests.for_include'


def test_setattr(obj):
    obj.include('tests.for_include')
    wrap = obj[0][1]
    wrap.val = 'var'

    assert wrap.val == 'var'
    assert obj.val == 'var'
