
FROM python:3.12-slim

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml
COPY ./app /code/app

RUN pip install --no-cache-dir uv
RUN uv pip install "fastapi[standard]" --system
RUN uv sync

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py"]