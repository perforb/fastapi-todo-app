# Overview

TBD

# Setup on local

```shell
mkdir .dockervenv

docker compose build

# Create pyproject.toml if it does not exist.
docker compose run \
--entrypoint "poetry init \
--name fastapi-todo-app \
--dependency fastapi \
--dependency uvicorn[standard]" \
fastapi-todo-app

# Installing dependencies from lock file
docker compose run --entrypoint "poetry install --no-root" fastapi-todo-app
```

# Launch on local

```shell
docker compose up
```
