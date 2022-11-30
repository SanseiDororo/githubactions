## Description

This repository covers GitHub Action basics. In the src folder it provides streamlit app
which can be used as a github actions cheat sheet. To run the app you need streamlit app which can be installed with the pipenv. To run the app

```
Run Github Cheat Sheet App.

streamlit run src/app.py
```


### Core elements

- Package configuration (Pipfile, Pipfile.lock)
- Makefile (install, develop, format, lint, test)


#### Makefile

Make file covers all the necessary parts for the installation, development and deployment
of the package.

#### Installing the project

**[Install]**

Install the package requirements

```
1. Upgrading PIP
2. Installing package requirements
```

#### Developing the project

**[Format]**

```
1. Formats all the existing python files in the repo.

Formater: Black
```

**[Lint]**

```
1. Analyse the code for the potential errors. Refactor and Convention
warnings are disabled. They can be turned on by removing the disable flag.
Warning: Refactor and Convenction warnings may cause builds to fail.

Linter: Pylint
```

**[Test]**

```
Performs dummy tests.

Tester:Pytest
```

#### To Do

- Add advanced parts of Github Actions.
- Provide real test scenarios.
- Create docker images.

#### Issues

