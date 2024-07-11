# github-clone

This microservice is listening to a AWS SQS queue waiting for messages. When it receives a message, it gets from its payload the GitHub repository URL, then it clones the repository and save it on a AWS S3 bucket.

![](.architecture.drawio.png)

- The payload of a message retrieved from the AWS SQS queue are shown below:
```json
{
    "repo_url": "https://github.com/user/public-repo-name.git"
}
```

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
cd ./microservices/github-clone
python main.py
```

> IMPORTANT: This MS requires an AWS SQS queue and a AWS S3 bucket to works. However, you can simulate this behavior without actually have those resources up by setting the environment variable ```DRY_RUN``` to ```True```.