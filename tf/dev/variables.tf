variable "aws_region" {
    type = string
    default = "us-east-1"
}

variable "github_api_version" {
    type = string
    default = "0.1.7"
}

variable "github_clone_version" {
    type = string
    default = "0.1.0"
}

variable "common_aws_sqs_queue_name" {
    type = string
    default = "github-repos-to-fork"
}
