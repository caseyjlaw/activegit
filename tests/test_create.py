import pytest
import activegit

def test_create0():
    with pytest.raises(TypeError):
        activegit.ActiveGit()

def test_create1():
    ag = activegit.ActiveGit('testrepo')
    assert ag.version == 'initial'

def test_create2():
    ag = activegit.ActiveGit('testrepo')
    assert ag.versions == ['initial']

def test_create3():
    ag = activegit.ActiveGit('testrepo')
    assert ag.isvalid == True

def test_create4():
    ag = activegit.ActiveGit('testrepo')
    ag = activegit.ActiveGit('testrepo')
    assert ag.isvalid == True

