Examples
########

activegit can be initialized by instantiating the base class with a path to a repo. If it does not exist, an empty repo will be filled::

    > ag = activegit.ActiveGit('agdir')
    ActiveGit initializing from repo at agdir
    Available versions: initial

After it has been initialized, features can be served to an expert for labeling (e.g., "real/bogus" or strings as tags). The features and corresponding target labels can then be saved::

    > ag.write_training_data(features, targets)
    > ag.write_classifier(clf)
    > ag.commit_version('newversion')
    > ag.versions
    ['initial', 'newversion']
