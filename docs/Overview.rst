Overview
########

activegit uses git to create shareable, distributable repositories of data and classifiers for active learning. activegit defines a Python class that casts some standard git features as methods that simplify the active learning proces. 

Active learning is a machine learning technique to iteratively train a classifier. The training of a classifier ("supervised learning") can be labor intensive, as it requires serving data to experts (people) for tagging. This work is often shared by several members of a group. The goal of activegit is to wrap git functionality (e.g., tags, push/pull) to simplify sharing and distribution of a repository that keeps track of data used to classify and the classifier itself.

An activegit repo has three basic files:

#. **training.pkl** -- A pickle file with a dictionary containing data to train the classifier. The dictionary length equal to the number of feature sets that have been labeled. Each feature set contains one or more features, but all feature sets must be the same size and match the number expected by the classifier.
#. **testing.pkl** -- Similar to training.pkl, but this file contains a dictionary used to test the classifier.
#. **classifier.pkl** -- A pickle file containing the classifier.

After initializing an activegit repo, the training, testing, and classifier pickle files are filled and committed with a version name. This version name is tied to a git tag, so it can be recalled at any time.

Installation
############

activegit is available via pypi, so simply::

    pip install activegit

.. toctree::
   :maxdepth: 2
