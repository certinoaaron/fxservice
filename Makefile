.PHONY: build
build:
	docker build . -t fxservice:latest

.PHONY: test
test:
	pytest -s -v