# ci-guide-example

Example Python unit testing code used as part of the Software Sustainability Institute's 
continuous integration guide which can be found at FIXME.

This basic exemplar requires Python 3.8 or above, uses the [pytest](https://pypi.org/project/pytest/) 
unit testing framework and [pytest-cov](https://pypi.org/project/pytest-cov/) to supply 
test coverage reports, and makes use of parameterised unit tests.


## Dependencies

The following have been used to build and test this example:

- Python 3.8.10
- pytest 6.2.5
- pytest-cov 3.0.0

See **Installation** below for instructions to install these dependencies.


## Installation

To use this repository as part of the guide, first select **Use this template** to create
your own copy of this repository, then (replacing **username** with your own GitHub username:

```
$ git clone https://github.com/username/ci-guide-example.git
```

Then, to set up the prerequisites:

```
$ cd ci-guide-example
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

## Running the unit tests

You can run the unit tests via:

```
$ python3 -m pytest --cov=mymath.factorial tests/test_factorial.py
```
