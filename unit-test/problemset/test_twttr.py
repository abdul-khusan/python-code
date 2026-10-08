from twttr import shorten
import pytest

def test_shorten():
      assert shorten('Twitter') == 'Twttr'

def test_uppercase():
      assert shorten('TWITTER') == 'TWTTR'

def test_lowercase():
      assert shorten('twitter') == 'twttr'

def test_str():
      with pytest.raises(TypeError):
            shorten(12)
