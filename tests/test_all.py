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
        assert len(testingd) == 2
        feats, targets = trainingd
        assert not len(feats)
        assert not len(targets)
        assert len(trainingd) == 2
        feats, targets = trainingd
        assert not len(feats)
        assert not len(targets)


    def test_write1(self, tmpdir):
        agdir = str(tmpdir.mkdir('tmp').realpath())
        ag = activegit.ActiveGit(agdir)
        features0 = [(1,2)]
        targets0 = [[0]]
        ag.write_testing_data(features, targets)
        features1 = [(3,4),]
        targets1 = [[1]]
        ag.write_training_data(features, targets)

        testingd0 = ag.testing_data
        trainingd0 = ag.training_data
        assert trainingd0 = [features0, targets0]
        assert testingd0 = [features1, targets1]
