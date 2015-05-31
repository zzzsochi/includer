import pytest

from includer import include


def test__includeme():
    data = []
    include('tests.for_include', data)

    assert len(data) == 1
    assert data[0] == ('includeme', data)


def test__func():
    data = []
    include('tests.for_include.func', data)

    assert len(data) == 1
    assert data[0] == ('func', data)


def test__real_func():
    from .for_include import func
    data = []
    include(func, data)

    assert len(data) == 1
    assert data[0] == ('func', data)


def test__not_found():
    with pytest.raises(ImportError):
        include('tests.for_include.not_exist')


def test__not_found_default():
    with pytest.raises(ImportError):
        include('tests.for_include', _default='not_exist')


def test__not_callable():
    with pytest.raises(TypeError):
        include('tests.for_include.not_callable')


def test__not_callable_defailt():
    with pytest.raises(TypeError):
        include('tests.for_include', _default='not_callable')


def test__rel_includeme():
    data = []
    include('.for_include', data, _module='tests')

    assert len(data) == 1
    assert data[0] == ('includeme', data)


def test__rel_func():
    data = []
    include('.for_include.func', data, _module='tests')

    assert len(data) == 1
    assert data[0] == ('func', data)


def test__rel_default_func():
    data = []
    include('.for_include', data, _module='tests', _default='func')

    assert len(data) == 1
    assert data[0] == ('func', data)
