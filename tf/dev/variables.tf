variable "aws_region" {
    type = string
    default = "us-east-1"
}

variable "github_api_version" {
    type = string
    default = "0.1.0"
}

variable "is_to_deploy_github_clone_as_lambda" {
    type = bool
    default = true
}

variable "github_clone_version" {
    type = string
    default = "0.1.0"
}

variable "common_aws_sqs_queue_name" {
    type = string
    default = "github-repos-to-fork"
}

variable "aws_s3_bucket_name" {
    type = string
    default = "repositories-edc1c5c1-1a23-4ca7-8458-4d70b4646318"
}
