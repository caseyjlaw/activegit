import pytest
import activegit

def test_nocreation():
    with pytest.raises(TypeError):
        activegit.ActiveGit()

def test_creation():
    ag = activegit.ActiveGit('testrepo')
    assert ag.version == 'initial'
