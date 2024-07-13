provider "aws" {
    region = var.aws_region
}

module "common" {
    source = "../modules/common"
    aws_sqs_queue_name = var.common_aws_sqs_queue_name
}

# module "github-api" {
#     source = "../modules/github-api"
#     depends_on = [ module.common ]
#     github_api_version = var.github_api_version
#     aws_region = var.aws_region
#     aws_default_vpc_id = module.common.default_vpc_id
#     aws_default_subnet_a_id = module.common.default_subnet_a_id
#     aws_default_subnet_b_id = module.common.default_subnet_b_id
#     aws_ecs_cluster_id = module.common.ecs_cluster_id
#     aws_sqs_queue_id = module.common.sqs_queue_id
#     aws_sqs_queue_arn = module.common.sqs_queue_arn
# }

module "github-clone" {
    count = var.is_to_deploy_github_clone_as_lambda == false ? 1 : 0
    source = "../modules/github-clone"
    depends_on = [ module.common ]
    github_clone_version = var.github_clone_version
    aws_region =var.aws_region
    aws_default_subnet_a_id = module.common.default_subnet_a_id
    aws_ecs_cluster_id = module.common.ecs_cluster_id
    aws_sqs_queue_id = module.common.sqs_queue_id
    aws_sqs_queue_arn = module.common.sqs_queue_arn
    aws_s3_bucket_name = var.aws_s3_bucket_name
}

module "gthub-clone-lambda" {
    count = var.is_to_deploy_github_clone_as_lambda == true ? 1 : 0
    source = "../modules/github-clone-lambda"
    aws_region = var.aws_region
    aws_sqs_queue_arn = module.common.sqs_queue_arn
    aws_s3_bucket_name = var.aws_s3_bucket_name
}
