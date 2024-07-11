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