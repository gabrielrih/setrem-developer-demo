import os

# Required
FORK_REPO_QUEUE_URL = os.getenv("FORK_REPO_QUEUE_URL")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Optional
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Optional
# DRY_RUN is to simulate without touching AWS (using fake implementation of some libraries)
DRY_RUN = os.getenv('DRY_RUN', False)
