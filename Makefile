.DEFAULT_GOAL := help

PACKAGE_VERSION := $(shell grep "version" package/pyproject.toml | grep -o "[0-9.]*")


.PHONY: test-kubot
test-kubot: ## Run kubot package tests
	@cd package && poetry run pytest tests --flake8

.PHONY: build-kubot
build-kubot: ## Build kubot package
	@cd package && poetry build


.PHONY: test
test: test-kubot ## Run all tests

.PHONY: build
build: build-kubot ## Build all


.PHONY: rebuild
rebuild: build-kubot ## rebuild kubot and reinstall it for the dispatcher
	@cd dispatcher \
		&& poetry remove kubot \
		&& poetry add ../package/dist/kubot-${PACKAGE_VERSION}-py3-none-any.whl
	@cd clients/example-bot \
		&& poetry remove kubot \
		&& poetry add ../../package/dist/kubot-${PACKAGE_VERSION}-py3-none-any.whl


.PHONY: help
help: ## Display this help
	@echo "Usage:\n  make \033[36m<target>\033[0m"
	@awk 'BEGIN {FS = ":.*##"}; \
		/^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } \
		/^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } \
		/^###@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
