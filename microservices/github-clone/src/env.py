import os

# Required
# FIX IT: We must receive it as environment variable instead of to have it fixed here
FORK_REPO_QUEUE_URL = os.getenv("FORK_REPO_QUEUE_URL", "https://sqs.us-east-1.amazonaws.com/533267331969/github-repos-to-fork")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "repositories-edc1c5c1-1a23-4ca7-8458-4d70b4646318")

# Optional
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Optional
# DRY_RUN is to simulate without touching AWS (using fake implementation of some libraries)
DRY_RUN = os.getenv('DRY_RUN', False)
