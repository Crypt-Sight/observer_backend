isort app/ && \
isort tests/ && \
black app/ && \
black tests/ && \
flake8 app/
flake8 tests/