import os

# Optional
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
# GITHUB_API_VERSION = os.getenv("GITHUB_API_VERSION", "-")

# Required
FORK_REPO_QUEUE_URL = os.getenv("FORK_REPO_QUEUE_URL", "https://sqs.us-east-1.amazonaws.com/533267331969/github-repos-to-fork")
