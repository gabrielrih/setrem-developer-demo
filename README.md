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

### Configuring AWS
- You must create an AWS account.
- You must create an user and an access key with admin privileges.
- Create a configuration file to be used by Terraform.

```sh
mkdir /Users/usuario/.aws
cp credentials /Users/usuario/.aws/
```

> This same configu file are used by ```aws cli```.

The configuration file will be similar to this:
```conf
[default]
aws_access_key_id=put my access key here
aws_secret_access_key=put my secret access key here
```

## Deploying on AWS

The creation of all the necessary resources plus the deploy of the microservices are done using Terraform.
```sh
cd tf/dev
terraform init
terraform plan
terraform apply --auto-approve
```

> Note that you must install terraform before run it.
