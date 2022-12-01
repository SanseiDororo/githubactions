## Description

This repository covers GitHub Action basics. In the src folder it provides streamlit app
which can be used as a github actions cheat sheet. To run the app you need streamlit app which can be installed with the pipenv. You can run the app with:

```
streamlit run src/app.py
```


### Core elements

- Package configuration (Pipfile, Pipfile.lock)
- Makefile (install, develop, format, lint, test)


#### Makefile

Makefile covers all the necessary parts for the installation, development and deployment
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

#### Github Workflows

Workflows stored under .github/workflows contain basic github actions. 

-  basic_workflow (Sets up runner and prints Hello world. Triggered manually on dispatch.)
-  add_existing_repo (Sets up runner and clone existing repository. Triggered mannualy on dispatch.)
- CICDpipenv (Sets up runner, clone repo, install pipenv, install development dependecies, perform code format, lint and test in the context of single runner environment. Triggered manually on discpatch.)
- CICDstructured (Sets up runners for: formating, linting, testing separately in a interdependent manner. If formating fails, linting is not executed.)

#### Issues

