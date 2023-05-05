# Define variables for commands
PYTHON_VERSION := python3
PIP := env/bin/pip
DJANGO := ./backend/DDF/manage.py
NPM := npm


install-pip:
	python -m ensurepip --upgrade

# Rule to install Python dependencies
deps: 
	$(PIP) install -r requirements.txt

# Rule to run Django migrations
migrate: 
	$(PYTHON_VERSION) $(DJANGO) makemigrations 
	$(PYTHON_VERSION) $(DJANGO) migrate 
	$(PYTHON_VERSION) $(DJANGO) migrate --database=test

test: 
	cd ./backend/DDF && $(PYTHON_VERSION) manage.py test --keepdb && cd .. && cd ..

# Rule to run the Django server
server: 
	$(PYTHON_VERSION) $(DJANGO) runserver

# Rule to install frontend dependencies
frontend:
	cd ./frontend && $(NPM) install && cd ..

# Rule to build the frontend
build: frontend
	cd ./frontend && $(NPM) run build && cd ..

# Rule to run all commands
all: deps migrate build server

.PHONY: deps migrate server frontend build all test

