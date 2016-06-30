import activegit
import pytest

def test_creation():
    with pytest.raises(TypeError):
        activegit.ActiveGit()
