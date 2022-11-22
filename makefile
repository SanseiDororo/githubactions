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
	black Intro/*py

lint:
	pylint --disable=R,C src/*.py

test:
	python -m pytest -vv 

build:
	docker build -t deploy-fastapi .

run:
	docker run -p 127.0.0.1:8080:8080 b205bf2bba68