.PHONY: build
build:
	docker build . -t fxservice:latest

.PHONY: test
test:
	pytest -s -v

.PHONY: format
format:
	black .

.PHONY: coverage
coverage:
	pytest --cov=app tests/