.PHONY: help install install-dev lint format format-check isort isort-check ruff ruff-fix mypy test test-cov test-html clean build quality check fix dev docs

help:  ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

# Installation
install:  ## Install the package in production mode
	uv sync

install-dev:  ## Install the package with dev dependencies
	uv sync --extra dev

# Linting and Formatting
lint:  ## Run flake8 linter
	uv run flake8 fastapi_ai_sdk tests examples

format:  ## Format code with black
	uv run black fastapi_ai_sdk tests examples

format-check:  ## Check if code is formatted correctly
	uv run black --check fastapi_ai_sdk tests examples

isort:  ## Sort imports with isort
	uv run isort fastapi_ai_sdk tests examples

isort-check:  ## Check if imports are sorted correctly
	uv run isort --check-only fastapi_ai_sdk tests examples

ruff:  ## Run ruff linter
	uv run ruff check fastapi_ai_sdk tests examples

ruff-fix:  ## Run ruff and auto-fix issues
	uv run ruff check --fix fastapi_ai_sdk tests examples

mypy:  ## Run type checking with mypy
	uv run mypy fastapi_ai_sdk --ignore-missing-imports

# Testing
test:  ## Run tests
	uv run pytest tests/ -v

test-quick:  ## Run tests quickly (minimal output)
	uv run pytest tests/ -q --tb=no

test-cov:  ## Run tests with coverage report
	uv run pytest tests/ --cov=fastapi_ai_sdk --cov-report=term-missing

test-html:  ## Run tests with HTML coverage report
	uv run pytest tests/ --cov=fastapi_ai_sdk --cov-report=html --cov-report=term
	@echo "📊 Coverage report generated at: htmlcov/index.html"

test-models:  ## Run model tests only
	uv run pytest tests/test_models.py -v

test-stream:  ## Run stream tests only
	uv run pytest tests/test_stream.py -v

test-integration:  ## Run integration tests only
	uv run pytest tests/test_fastapi_integration.py -v

# Development Servers
dev:  ## Run simple chat example server
	uv run uvicorn examples.simple_chat:app --reload

dev-advanced:  ## Run advanced assistant example server
	uv run uvicorn examples.advanced_ai_assistant:app --reload

dev-llm:  ## Run LLM integration example server
	uv run uvicorn examples.llm_integration:app --reload

# Build and Distribution
build:  ## Build distribution packages
	uv run python -m build

build-check:  ## Check distribution packages
	uv run twine check dist/*

clean:  ## Clean build artifacts and cache
	rm -rf build dist *.egg-info .coverage htmlcov .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".DS_Store" -delete

# Combined Commands
quality:  ## Run all formatters and linters (fix mode)
	@echo "🎨 Formatting code with black..."
	@$(MAKE) format
	@echo "📦 Sorting imports with isort..."
	@$(MAKE) isort
	@echo "🔍 Running flake8..."
	@$(MAKE) lint
	@echo "🔧 Running ruff..."
	@$(MAKE) ruff
	@echo "🔎 Running mypy..."
	@$(MAKE) mypy
	@echo "✅ Quality checks complete!"

check:  ## Run all quality checks (no fixes)
	@echo "🔍 Checking code quality..."
	@$(MAKE) format-check
	@$(MAKE) isort-check
	@$(MAKE) lint
	@$(MAKE) ruff
	@$(MAKE) mypy
	@echo "✅ All checks passed!"

fix:  ## Auto-fix all possible issues
	@echo "🔧 Auto-fixing issues..."
	@$(MAKE) format
	@$(MAKE) isort
	@$(MAKE) ruff-fix
	@echo "✅ Auto-fix complete!"

# Documentation
docs:  ## Open documentation
	@echo "📚 Documentation at: https://github.com/doganarif/fastapi-ai-sdk#readme"
	@echo ""
	@echo "Available Make targets:"
	@$(MAKE) help
