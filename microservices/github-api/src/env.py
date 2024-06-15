import os

# Optional
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
GITHUB_API_VERSION = os.getenv("GITHUB_API_VERSION", "-")
FLASK_PORT = os.getenv("FLASK_PORT", 3000)

# Required
FORK_REPO_QUEUE_URL = os.getenv("FORK_REPO_QUEUE_URL", None)