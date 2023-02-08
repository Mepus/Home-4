import pytest
from string_utils import StringUtils

stringutils = StringUtils()

@pytest.mark.parametrize("text, result", [("skypro", "Skypro")])
def test_capitilize(text, result):
    stringutils = StringUtils
    res = stringutils.capitilize(text, result)
    assert res == result


@pytest.mark.parametrize("text, result", [(" skypro", "skypro")])
def test_trim(text, result):
    stringutils = StringUtils
    res = stringutils.trim(text, result)
    assert res == result

@pytest.mark.parametrize("text, delimeter, result", [("a,b,c,d", ["a", "b", "c", "d"])])
def test_to_list(text, delimeter, result):
    stringutils = StringUtils
    res = stringutils.to_list(text, delimeter)
    assert res == result

@pytest.mark.parametrize("text, symbol, result", [("SkyPro", "U")])
def test_contains(text, symbol, result):
    stringutils = StringUtils
    res = stringutils.contains(text, symbol)
    assert res == result

@pytest.mark.parametrize("text, symbol, result", [("SkyPro", "k",)])
def test_delete_symbol(text, symbol, result):
    stringutils = StringUtils
    res = stringutils.delete_symbol(text, symbol)
    assert res == result


@pytest.mark.parametrize("text, symbol, result", [("SkyPro", "S",)])
def test_starts_with(text, symbol, result):
    stringutils = StringUtils
    res = stringutils.starts_with(text, symbol)
    assert res == result

@pytest.mark.parametrize("text, result", [("SkyPro", "o",)])
def test_is_empty(text, result):
    stringutils = StringUtils
    res = stringutils.starts_with(text, result)
    assert res == result

@pytest.mark.parametrize("text, result", [1,2,3,4] "1, 2, 3, 4")
def test_list_to_string(text, result):
    stringutils = StringUtils
    res = stringutils.starts_with(text, result)
    assert res == result