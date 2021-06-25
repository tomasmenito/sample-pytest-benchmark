FROM python:3.8.6-slim-buster

RUN pip install poetry

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    tzdata \
    && \
    rm -rf /var/lib/apt/lists/*

ARG POETRY_HTTP_BASIC_OLIST_USERNAME
ARG POETRY_HTTP_BASIC_OLIST_PASSWORD
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD . /app/

ENTRYPOINT ["python", "-m", "python_project_template"]
