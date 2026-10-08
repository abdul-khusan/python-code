from plate import is_valid
import pytest

def test_shorten():
      assert is_valid('aaa44') == True

def test_middlenum():
      assert is_valid('aa44aa') == False

def test_nospace():
      assert is_valid('aa 44aa') == False

def test_zerofirst():
      assert is_valid('AA0') == False

def test_fourchar():
      assert is_valid('AA12') == True

def test_nochar():
      assert is_valid('AA!23') == False

def test_str():
      with pytest.raises(TypeError):
            is_valid(0)
