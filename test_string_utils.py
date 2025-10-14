import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",

                         [
                             ("skypro", "Skypro"),
                             ("hello world", "Hello world"),
                             ("python", "Python"),
                         ])

def test_capitalize_positive(input_str,expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",
                         [
                             ('123abc','123abc'),
                             ('',''),
                             ('   ', '   '),

                         ])
def test_capitalize_negative(input_str,expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",
                         [
                             (" SkyPro", "SkyPro"),
                             ("  two", "two"),
                             ("   .", ".")
                         ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",
                         [
                             ("нет пробела в начале", "нет пробела в начале"),
                             ("1 2", "1 2"),
                             ("",""),

                         ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",

                         [
                             ("skypro", "s"),
                             ("hello world", "l"),
                             ("python", "t"),
                         ])
def test_capitalize_contains(input_str,expected):
    assert string_utils.contains(input_str) == expected


@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize("input_str, expected",
                         [
                             ('skypro','a'),
                             ('Hello','h'),
                             ('world', '123'),

                         ])
def test_capitalize_contains(input_str,expected):
    assert string_utils.contains(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, delete_symbol, expected",

                         [
                             ("Один", "О", "дин"),
                             ("jelly!", "!", "jelly"),
                             ("погода", "о", "пгда"),
                         ])

def test_delete_symbol(input_str, delete_symbol, expected):
    assert string_utils.delete_symbol(input_str, delete_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, delete_symbol, expected",
                         [
                             ("параметр","я", "параметр"),
                             ('12345','6', '12345'),
                             ('!&^^&&', '*', '!&^^&&'),

                         ])
def test_delete_symbil(input_str,delete_symbol, expected):
    assert string_utils.delete_symbol(input_str, delete_symbol) == expected