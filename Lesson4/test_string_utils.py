from typing import Literal
import pytest 
from string_utils import StringUtils

string_utils = StringUtils


@pytest.mark.parametrize('string, result', [("hello", "Hello"), ("удачного дня", "Удачного дня"), ("456", "456")])
def test_positive__capitilize(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("", ""), (None, None), (123, 123)])
def test_negative__capitilize(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.capitilize()

@pytest.mark.parametrize('string, result', [(" Ksenia", "Ksenia"), (" Утро", "Утро")])
def test_positive__trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, result', [(None, None), (345, 345)])
def test_negative__trim(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.trim()

@pytest.mark.parametrize('string, delimeter, result',[("а,б,в,г", ",", ["а","б", "в","г"]), ("8:4:3",":", ["8", "4", "3"])])
def test_positive__to_list(string, delimeter, result,):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string, result', [(None, None), (456789876, 456789876)])
def test_negative__to_list(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.to_list()

@pytest.mark.parametrize('string, symbol, result',[("Hello", "H", True), ("1,2,3,4", "1", True), ("Good morning", "m", False)])
def test_positive__contains(string, symbol, result,):
    string_utils = StringUtils()
    result = string_utils.contains(string, symbol)
    result = False
    try:
        result = string.index(symbol)
    except ValueError:
        pass
    assert result == result

@pytest.mark.parametrize('string, result', [([],[]),(None, None), (-123, -123)])
def test_negative__contains(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.contains()

@pytest.mark.parametrize('string, symbol, result',[("Ксения", "К", "сения"), ("Love_you", "_you", "Love")])
def test_positive__delete_symbol(string, symbol, result,):
    string_utils = StringUtils()
    if(string_utils.delete_symbol(string, symbol)):
            string = string.replace(symbol, "")    
    assert string == result 

@pytest.mark.parametrize('string, result', [([],[]),(None, None), (1234567890, 1234567890)])
def test_negative__delete_symbol(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.delete_symbol()

@pytest.mark.parametrize('string, symbol, result',[("Hello","H",True),("Morogova","M",True),("SkyPro", "k", False),("Telegram", "g",False)])
def test_positive__starts_with(string, symbol, result):
    string_utils = StringUtils()
    result = string_utils.starts_with(string,symbol)
    assert result == result

@pytest.mark.parametrize('string, result', [(12345, 12345),(None, None)])
def test_negative__starts_with(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.starts_with()

@pytest.mark.parametrize('string, symbol, result',[("Hello","o",True),("Ksenia","a",True),("Привет", "в", False),("Часы", "ч",False)])
def test_positive__end_with(string, symbol, result):
    string_utils = StringUtils()
    result = string_utils.end_with(string,symbol)
    assert result == result

@pytest.mark.parametrize('string, result', [([],[]),(None, None)])
def test_negative__end_with(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.end_with()

@pytest.mark.parametrize('string, result', [("",True),(" ",True),("Хороший день", False),("car",False)])
def test_positive__is_empty(string, result):
    string_utils = StringUtils()
    result = string_utils.is_empty(string)
    assert result == result

@pytest.mark.parametrize('string, result', [([],[]),(None, None), (1234554, 1234554)])
def test_negative__is_empty(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.is_empty()

@pytest.mark.parametrize('string, words, result', [(["Kse","nia"], ":", "Kse:nia"),(["Выполнить", "домашнюю","работу"], " ", "Выполнить домашнюю работу"),(["987", "123"], "*", "987*123")])
def test_positive__list_to_string(string, words, result):
    string_utils = StringUtils()
    result = string_utils.list_to_string(string, words)
    assert result == result

@pytest.mark.parametrize('string, result', [(None, None), ("","")])
def test_negative__list_to_string(string, result):
    string_utils = StringUtils()
    with pytest.raises(Exception):
        string_utils.list_to_string()