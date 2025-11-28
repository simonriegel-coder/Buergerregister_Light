.PHONY: install lint format test coverage ci

install:
	pip install -e .[dev]

lint:
	ruff check src tests
	isort . --check-only
	black --check .

format:
	isort .
	black .

test:
	pytest -q

coverage:
	pytest --cov=src/buergerregister --cov-branch --cov-report=html

ci:
	make lint
	make test
	make coverage
