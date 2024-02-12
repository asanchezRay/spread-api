VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python
COVERAGE := $(VENV_DIR)/bin/coverage
TESTS := $(wildcard tests/*/test_*.py)

.PHONY: test

test: $(PYTHON) venv
	$(PYTHON) -m pip install -r requirements.txt && \
	$(PYTHON) -m coverage run -m unittest $(TESTS) && \
	$(PYTHON) -m coverage html

venv: $(PYTHON)

$(PYTHON):
	python3 -m venv $(VENV_DIR)

clean:
	rm -rf $(VENV_DIR)

build:
	docker build -t spread_api .

run:
	docker run -d -p 8000:8000 spread_api
