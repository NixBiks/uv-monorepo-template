# Define the Python command to run in each directory
PYTEST_COMMAND := uv run pytest  # Replace with your actual Python command

# Find all directories containing pyproject.toml
PYPROJECT_DIRS := $(shell find . -name pyproject.toml -not -path "./pyproject.toml" -exec dirname {} \;)

# Run pytest in all apps/packages in an isolated environment
test: $(PYPROJECT_DIRS)
	@EXIT_CODE=0; \
	for dir in $(PYPROJECT_DIRS); do \
	    (cd $$dir && uv sync > /dev/null 2>&1 && $(PYTEST_COMMAND) > /dev/null 2>&1 || { echo "$$dir: Failed"; $(PYTEST_COMMAND); EXIT_CODE=1; }); \
	done; \
	uv sync > /dev/null 2>&1; \
	[ $$EXIT_CODE -eq 0 ] && echo "All tests passed" || echo "Some tests failed"; \
	exit $$EXIT_CODE

format:
	@uv run ruff format

lint:
	@uv run ruff check

.PHONY: format lint test