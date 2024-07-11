# github-api

This microservice offers some endpoints to performe some actions against GitHub users and public repositories on GitHubs.

See [./src/env](./src/env.py) to know the required environment variables.

## Endpoints

### GET /_health

```/_health```

Internal endpoint for check the health of the microservices.

### GET /github-user

```/github-user&username=gabrielrih```

It returns information about an specific user.

### GET /github-user-repos

```/github-user-repos&username=gabrielrih```

It returns the list of public repositories from an specific user.

### GET /clone-repo

```/clone-repo&repo_url=https://github.com/user/public-repo-name.git```

It schedule to clone an specific public repository from GitHub.

> The service which in fact clones the repository is the microservice [github-clone](../github-clone/README.md).


## How to test on local machine

You must create a ```.env``` file on the root path and set all the required environment variables using this format:
```
ENVIRONMENT_VARIABLE_NAME="value"
```

> See [./src/env.py](./src/env.py) to know all the possible environment variables.


Now you can start the Python virtual environment by running these commands:

```sh
poetry install --no-root
poetry shell
```

> To allow you to run this microservice in your machine you must guarantee that all the libraries dependencies are specified on [pyproject.toml](./pyproject.toml) file.

Finally, just starts the microservice by running:
```sh
cd ./microservices/github-api
python -m flask run --port=3000 --host=0.0.0.0
```

> IMPORTANT: This MS requires an AWS SQS queue to works. However, you can simulate this behavior without actually have this resource up by setting the environment variable ```DRY_RUN``` to ```True```.