install:
	@echo "Updating pip and installing project dependecies"
	pip install --upgrade pip &&\
	pipenv install -e .

develop:
	@echo "Installing development packages"
	@echo "Formating:Black | Linting:Pylint | Testing:Pytest"

	pipenv install --dev black pylint pytest 

format:
	black *.py 
	black src/Intro/*py

lint:
	pylint --disable=R,C src/Intro/*.py

test:
	python -m pytest -vv 

