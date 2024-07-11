variable "github_clone_version" {
    type = string
}

variable "aws_region" {
    type = string
}

variable "aws_default_subnet_a_id" {
    type = string
}

variable "aws_sqs_queue_id" {
    type = string
}

variable "aws_sqs_queue_arn" {
    type = string
}

variable "aws_s3_bucket_name" {
    type = string
    default = "repositories-edc1c5c1-1a23-4ca7-8458-4d70b4646318"
}
