FROM python:3.13

WORKDIR /app

RUN pip install poetry && poetry --version

COPY . .

COPY pyproject.toml poetry.lock README.md ./

ENV PIP_DEFAULT_TIMEOUT=300
ENV POETRY_HTTP_TIMEOUT=300

RUN poetry install

EXPOSE 8000



CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]