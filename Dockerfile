
FROM python:3.12-slim

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml
COPY ./app /code/app

RUN pip install --no-cache-dir uv
RUN uv sync

EXPOSE 8000

RUN uv run alembic upgrade head

CMD ["uv","run","fastapi", "run", "app/main.py"]