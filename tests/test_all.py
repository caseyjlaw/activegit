import pytest
import activegit

class TestClass_create:

    def test_create0(self):
        with pytest.raises(TypeError):
            ag = activegit.ActiveGit()


    def test_create1(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        assert ag.version == 'initial'


    def test_create2(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        assert ag.versions == ['initial']


    def test_create3(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        assert ag.isvalid == True


    def test_create4(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        ag = activegit.ActiveGit(agdir)
        assert ag.isvalid == True

class TestClass_versions:

    def test_set0(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)

        with pytest.raises(AttributeError):
            ag.set_version('blah')


    def test_set1(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        ag.set_version('initial')


    def test_set2(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        ag.set_version('initial', force=True)

class TestClass_write:

    def test_write0(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        testingd = ag.testing_data
        trainingd = ag.training_data
        assert not len(testingd)
        assert not len(trainingd)


    def test_write1(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        testingd = {[1,2,3]: 0}
        trainingd = {[4,5,6]: 1}
        ag.write_testing_data(testingd)
        ag.write_training_data(trainingd)
        testingd0 = ag.testing_data
        trainingd0 = ag.training_data
        assert testingd == testingd0
        assert trainingd == trainingd0
