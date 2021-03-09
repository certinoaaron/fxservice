FROM python:3.9 as base

# setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

RUN pip install pipenv
RUN apt update && apt install -y --no-install-recommends

# install python deps in .venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

# Copy venv from python-deps
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
COPY Pipfile.lock .
RUN pipenv install

# install app into container
WORKDIR /app
COPY /app .

# Run the app
ENTRYPOINT ["flask" , "run" ,"--host=0.0.0.0", "--port=5100"]