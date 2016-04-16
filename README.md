# activegit
Using git repos for distributed for active learning

# Usage
    ag = activegit.ActiveGit(repopath)
    ActiveGit initializing from repo at <repopath>
    Available versions: initial

(Build up targets for features. Update classifier.)

    ag.write_training_data(features, targets)
    ag.write_classifier(clf)
    ag.commit_version('newversion')
    ag.versions
    ['initial', 'newversion']
    ag.set_version('newversion')

# Install
    python setup.py install
