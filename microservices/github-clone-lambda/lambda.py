import json
import os
import boto3

from git import Repo


files_limit = 500
s3 = boto3.client("s3")


def handler(event, _):
    print(f'{event =}')

    body = event["Records"][0]["body"]
    body = json.loads(body)
    repo_url = body['repo_url']
    extension = body['extension']
    print(f'{repo_url =} {extension =}')

    repo_name = repo_url.split('/')[-1].replace('.git', '')

    local_path = f'/tmp/{repo_name}'
    Repo.clone_from(
        url = repo_url,
        to_path = local_path,
        depth = 1
    )
    copy_to_s3(
        source_path = local_path,
        target_path = repo_name,
        extension = extension
    )

    return event


def copy_to_s3(source_path: str, target_path: str, extension: str):
    count = 0
    bucket_name = os.getenv("S3_BUCKET_NAME")
    for root, dirs, files in os.walk(source_path):
        if ".git" in dirs:
            dirs.remove(".git")
        for file in files:
            if extension and not file.endswith(extension):
                continue
            if count >= files_limit:
                print(f'Files limit reached. Skipping {root}/{file}')
                break
            file_path = os.path.join(root, file)
            s3_path = file_path.replace(source_path, target_path)
            print(f"Uploading {file_path} to s3://{bucket_name}{s3_path}")
            s3.upload_file(file_path, bucket_name, s3_path)
            count += 1
