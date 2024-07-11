variable "github_api_version" {
    type = string
}

variable "github_api_internal_port" {
    type = number
    default = 3000
}

variable "aws_region" {
    type = string
}

variable "aws_default_vpc_id" {
    type = string
}

variable "aws_default_subnet_a_id" {
    type = string
}

variable "aws_default_subnet_b_id" {
    type = string
}

variable "aws_ecs_cluster_id" {
    type = string
}

variable "aws_sqs_queue_id" {
    type = string
}

variable "aws_sqs_queue_arn" {
    type = string
}
