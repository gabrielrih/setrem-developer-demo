## Setrem developer demo

Demo activity to create and deploy on AWS some microservices.

## How to run tests

We are using [Poetry](https://python-poetry.org/) for manage the Python dependencies and I recommend the use of [pyenv](https://github.com/pyenv/pyenv) or other tool to manage Python versions.

Before you run anything in your machine just run these commands to start the Python virtual environment:

```sh
poetry install --no-root
poetry shell
```

Then, you can run all the tests by executing this command:
```sh
pytest
```

> To allow you to run the tests in your machine you must guarantee that all the libraries dependencies are specified on [pyproject.toml](./pyproject.toml) file.


## Deploying on AWS
TO DO

<!--
- Credenciais da AWS
- Instalar TerraForm e Docker na máquina.
-->
