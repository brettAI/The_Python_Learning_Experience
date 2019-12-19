# The Python Learning Experience

A ongoing record or my Python Learning Experience. This repository will track my learning as I progress from noob to......

From here I will track

- [The Python Learning Experience](#the-python-learning-experience)
  - [Ultimate Goal](#ultimate-goal)
  - [Learning Assumptions](#learning-assumptions)
    - [Development Environment](#development-environment)
  - [Areas of Focus](#areas-of-focus)
    - [Python](#python)
      - [Python Packages](#python-packages)
    - [Finance](#finance)
  - [Online/Offline Learning Resources](#onlineoffline-learning-resources)
  - [Sample Projects](#sample-projects)

## Ultimate Goal

My Ultimate Goal for learning Python is to develop a financial assets trading system that will use a number of techniques to:

- predict price movements
- construction of various portfolios (different risk profiles)
- management of the portfolio

Code specific to this ultimate goal will be stored in the Xybele repository.

## Learning Assumptions

The following assumptions (guidelines) will be used to facilitate and direct my learning.

- Documents (readme files, tracking documents, requirements, etc) will be written in Markdown
- Linting - pyLint

### Development Environment

- [Microsoft Visual Studio Code](https://code.visualstudio.com/) is my editor of choice. In addition to using VS Code, the following extensions will be used:
  - Python by Microsoft
  - markdownlint - Provide realtime lint advise for Markdown files
  - pylint - Linting is the processing of identifying problems in syntax or style of a program.
  - autopep8 for formatting (VS Code will run this by default but it can be run as `python -m pip install -U autopep8`)
  - Extension `Code Runner` to enable fast running of Python programs. **Needs to be setup to use the Virtual Environment**

```json
    "code-runner.executorMap": {
        "python": "$pythonPath -u $fullFileName"
    },
    "code-runner.clearPreviousOutput": true,
```

Need to Look at:
- pyinstaller
- nsis - convert a zip file into a deployable/installable executable.


## Areas of Focus

My ultimate goal will require a detailed understanding across of number of domains.

### Python

- Use the timeit package to determine the time code takes to run.

#### Python Packages

- [NumPy](https://numpy.org/) - a package for scientific computing with Python
- [Pandas](https://pandas.pydata.org/) - a package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python.
- [SciPy](https://docs.scipy.org/doc/scipy/reference/index.html#) - open-source software for mathematics, science, and engineering.
- [Scikit_Learn](https://scikit-learn.org/stable/) - Simple and efficient tools for data mining and data analysis
- [pipenv](https://pypi.org/project/pipenv/) - Create and manage a virtualenv for python projects

### Finance

## Online/Offline Learning Resources

- [Videos](Learning/VIDEOS.md)
- [Online Tutorials](Learning/TUTORIALS.md)
- [Books](Learning/BOOKS.md)

## Sample Projects
